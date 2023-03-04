from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_to_chat_keyboard(text: str, link: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=text, url=link),
            ],
        ]
    )
