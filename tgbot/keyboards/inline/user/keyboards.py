from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.keyboards.inline.common.callbacks import ResidentialComplexCallbackFactory
from tgbot.keyboards.inline.common.keyboards import create_back_button

from tgbot.models.house import House
from tgbot.models.residential_complex import ResidentialComplex
from tgbot.utils.formatting import house_format


def create_choice_residential_complex_keyboard(residential_complexes: list[ResidentialComplex]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for residential_complex in residential_complexes:
        builder.row(
            InlineKeyboardButton(
                text=residential_complex.title,
                callback_data=ResidentialComplexCallbackFactory(residential_complex_id=residential_complex.id).pack(),
            )
        )

    builder.row(create_back_button())

    return builder.as_markup()


def create_choice_house_keyboard(houses: list[House]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for house in houses:
        builder.row(InlineKeyboardButton(text=house_format(house), url=house.link_chat))

    builder.row(create_back_button())

    return builder.as_markup()
