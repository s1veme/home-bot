import types

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from tgbot.keyboards.inline.admin.callbacks import AdminMenuCallbackFactory
from tgbot.keyboards.inline.common.callbacks import DistrictCallbackFactory, ResidentialComplexCallbackFactory
from tgbot.keyboards.inline.common.keyboards import (
    create_select_district_keyboard,
    create_select_residential_complex_keyboard,
)
from tgbot.misc.states import CreateHouse
from tgbot.models.district import DistrictEnum
from tgbot.models.house import House
from tgbot.services.house import HouseService
from tgbot.services.residential_complex import ResidentialComplexService

router = Router()

residential_complex_service: ResidentialComplexService = ResidentialComplexService.get_instance()
house_service: HouseService = HouseService.get_instance()


@router.callback_query(AdminMenuCallbackFactory.filter(F.action == 'create_house'))
async def create_house(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        'Выберите район', reply_markup=create_select_district_keyboard(DistrictEnum.list())
    )

    await state.set_state(CreateHouse.district)

    await callback.answer()


@router.callback_query(CreateHouse.district, DistrictCallbackFactory.filter())
async def select_district(callback: types.CallbackQuery, callback_data: DistrictCallbackFactory, state: FSMContext):
    await state.set_state(CreateHouse.residential_complex)

    residential_complexes = await residential_complex_service.get_all_residential_complex_by_district(
        callback_data.district
    )

    await callback.message.edit_text(
        'Отлично! Выберите ЖК:', reply_markup=create_select_residential_complex_keyboard(residential_complexes)
    )

    await callback.answer()


@router.callback_query(CreateHouse.residential_complex, ResidentialComplexCallbackFactory.filter())
async def select_district(
    callback: types.CallbackQuery, callback_data: ResidentialComplexCallbackFactory, state: FSMContext
):
    await state.update_data(residential_complex_id=callback_data.residential_complex_id)
    await state.set_state(CreateHouse.numbers)

    await callback.message.edit_text('Отлично! Введите диапазон домов в формате 10-20:')

    await callback.answer()


@router.message(CreateHouse.numbers, F.text.regexp(r'^\d+[\s+]?-[\s+]?\d+$'))
async def input_number(message: types.Message, state: FSMContext):
    await state.set_state(CreateHouse.link_chat)

    start_number, end_number = list(map(int, message.text.replace(' ', '').split('-')))
    await state.update_data(start_number=start_number)
    await state.update_data(end_number=end_number)

    await message.answer('Хорошо! Введите ссылку на чат:')


@router.message(CreateHouse.numbers, ~F.text.regexp(r'^\d+[\s+]?-[\s+]?\d+$'))
async def input_number_invalid(message: types.Message, state: FSMContext):
    await message.answer('Пожалуйста, введите диапазон домов в валидном формате: 1-10')


@router.message(CreateHouse.link_chat)
async def input_link_chat(message: types.Message, state: FSMContext):
    link_chat = message.text
    data = await state.get_data()

    house = House(
        link_chat=link_chat,
        start_house=data['start_number'],
        end_house=data['end_number'],
        residential_complex_id=data['residential_complex_id'],
    )

    await house_service.create(house)

    await message.answer('Дом успешно создан!')

    await state.clear()
