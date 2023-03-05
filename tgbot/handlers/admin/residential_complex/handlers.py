from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from tgbot.keyboards.inline.admin.callbacks import AdminMenuCallbackFactory
from tgbot.keyboards.inline.common.callbacks import DistrictCallbackFactory, ResidentialComplexCallbackFactory
from tgbot.keyboards.inline.common.keyboards import (
    create_back_keyboard,
    create_select_district_keyboard,
)
from tgbot.misc.states import CreateResidentialComplex, DeleteResidentialComplex
from tgbot.models.district import DistrictEnum
from tgbot.models.residential_complex import ResidentialComplex
from tgbot.services.residential_complex import ResidentialComplexService

router = Router()


residential_complex_service: ResidentialComplexService = ResidentialComplexService.get_instance()


@router.callback_query(AdminMenuCallbackFactory.filter(F.action == 'create_residential_complex'))
async def create_residential_complex(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        'Выберите район:', reply_markup=create_select_district_keyboard(DistrictEnum.list())
    )
    await state.set_state(CreateResidentialComplex.district)

    await callback.answer()


@router.callback_query(CreateResidentialComplex.district, DistrictCallbackFactory.filter())
async def select_district(callback: types.CallbackQuery, callback_data: DistrictCallbackFactory, state: FSMContext):
    await state.update_data(district=callback_data.district)
    await state.set_state(CreateResidentialComplex.title)

    await callback.message.edit_text('Введите название ЖК:')

    await callback.answer()


@router.message(CreateResidentialComplex.title)
async def input_title(message: types.Message, state: FSMContext):
    district = (await state.get_data())['district']
    title = message.text

    await residential_complex_service.create(
        ResidentialComplex(
            title=title,
            district=district,
        )
    )

    await message.answer('ЖК успешно создан!')
    await state.clear()


@router.callback_query(AdminMenuCallbackFactory.filter(F.action == 'remove_residential_complex'))
async def select_district_for_delete_complex(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        'Выберите район:', reply_markup=create_select_district_keyboard(DistrictEnum.list())
    )
    await state.set_state(DeleteResidentialComplex.district)

    await callback.answer()


@router.callback_query(DistrictCallbackFactory.filter(), DeleteResidentialComplex.district)
async def select_residential_complex_for_delete(
    callback: types.CallbackQuery, callback_data: DistrictCallbackFactory, state: FSMContext
):
    await state.set_state(DeleteResidentialComplex.residential_complex_id)

    residential_complexes = await residential_complex_service.get_all_residential_complex_by_district(
        callback_data.district
    )
    await callback.message.edit_text(
        'Отлично! Выберите ЖК:', reply_markup=create_select_xresidential_complex_keyboard(residential_complexes)
    )


@router.callback_query(DeleteResidentialComplex.residential_complex_id, ResidentialComplexCallbackFactory.filter())
async def delete_residential_complex(
    callback: types.CallbackQuery, callback_data: ResidentialComplexCallbackFactory, state: FSMContext
):
    await residential_complex_service.delete(callback_data.residential_complex_id)
    await callback.message.edit_text('ЖК успешно удалён', reply_markup=create_back_keyboard())
    await callback.answer()
    await state.clear()
