from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.keyboards.inline.admin.callbacks import AdminMenuCallbackFactory


def create_menu_admin_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Создать ЖК',
                    callback_data=AdminMenuCallbackFactory(action='create_residential_complex').pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text='Удалить ЖК',
                    callback_data=AdminMenuCallbackFactory(action='remove_residential_complex').pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text='Создать дом',
                    callback_data=AdminMenuCallbackFactory(action='create_house').pack(),
                )
            ],
        ]
    )
