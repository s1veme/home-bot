from aiogram import Router, types, F

from tgbot.handlers.user.start import start as user_start
from tgbot.keyboards.inline.common.callbacks import MenuCallbackFactory

common_router = Router()


@common_router.callback_query(MenuCallbackFactory.filter(F.action == 'back'))
async def go_to_menu(callback: types.CallbackQuery):
    await user_start(callback.message, is_edit=True)

    await callback.answer()
