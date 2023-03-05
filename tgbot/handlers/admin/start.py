from aiogram import types

from tgbot.keyboards.inline.admin.keyboards import create_menu_admin_keyboard


async def start(message: types.Message, is_edit: bool = False):
    if is_edit:
        message_method = message.edit_text
    else:
        message_method = message.answer

    await message_method('Что вы хотите сделать?', reply_markup=create_menu_admin_keyboard())
