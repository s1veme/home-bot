from aiogram import types

from tgbot.keyboards.inline.common.keyboards import create_select_district_keyboard
from tgbot.models.district import DistrictEnum
from tgbot.services.residential_complex import ResidentialComplexService

residential_complex_service: ResidentialComplexService = ResidentialComplexService.get_instance()


async def start(message: types.Message, is_edit: bool = False):
    if is_edit:
        message_method = message.edit_text
    else:
        message_method = message.answer

    await message_method('Выберите район:', reply_markup=create_select_district_keyboard(DistrictEnum.list()))
