from aiogram import Router, types

from tgbot.keyboards.inline.common.keyboards import create_to_chat_keyboard
from tgbot.keyboards.inline.user.callbacks import (
    DistrictCallbackFactory,
    HouseCallbackFactory,
    ResidentialComplexCallbackFactory,
)
from tgbot.keyboards.inline.user.keyboards import (
    create_choice_house_keyboard,
    create_choice_residential_complex_keyboard,
)
from tgbot.services.house import HouseService
from tgbot.services.residential_complex import ResidentialComplexService

router = Router()

residential_complex_service: ResidentialComplexService = ResidentialComplexService.get_instance()
house_service: HouseService = HouseService.get_instance()


@router.callback_query(DistrictCallbackFactory.filter())
async def get_residential_complex_by_district(callback: types.CallbackQuery, callback_data: DistrictCallbackFactory):
    residential_complex = await residential_complex_service.get_all_residential_complex_by_district(
        callback_data.district
    )
    await callback.message.edit_text(
        'Выберите ЖК:', reply_markup=create_choice_residential_complex_keyboard(residential_complex)
    )
    await callback.answer()


@router.callback_query(ResidentialComplexCallbackFactory.filter())
async def get_house_by_residential_complex(
    callback: types.CallbackQuery, callback_data: ResidentialComplexCallbackFactory
):
    houses = await house_service.get_houses_by_residential_complex(callback_data.residential_complex_id)

    await callback.message.edit_text('Выберите дом:', reply_markup=create_choice_house_keyboard(houses))

    await callback.answer()


@router.callback_query(HouseCallbackFactory.filter())
async def get_link_chat_by_house(callback: types.CallbackQuery, callback_data: HouseCallbackFactory):
    house = await house_service.get_house_by_id(callback_data.house_id)

    await callback.message.edit_text(
        'Тыкните на кнопочку, чтобы перейти в чат:', reply_markup=create_to_chat_keyboard('Чат', house.link_chat)
    )
    await callback.answer()
