from aiogram import types

from tgbot.keyboards.inline.user.keyboards import create_menu_user_keyboard
from tgbot.models.district import DistrictEnum
from tgbot.services.residential_complex import ResidentialComplexService

residential_complex_service: ResidentialComplexService = ResidentialComplexService.get_instance()


async def start(message: types.Message):
    await message.reply('Выберите район:', reply_markup=create_menu_user_keyboard(DistrictEnum.list()))
