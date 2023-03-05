from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.keyboards.inline.common.callbacks import (
    DistrictCallbackFactory,
    MenuCallbackFactory,
    ResidentialComplexCallbackFactory,
)
from tgbot.models.residential_complex import ResidentialComplex


def create_back_button() -> InlineKeyboardButton:
    return InlineKeyboardButton(text='В меню', callback_data=MenuCallbackFactory(action='back').pack())


def create_back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=create_back_button())


def create_select_district_keyboard(districts: list[str]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for district in districts:
        builder.row(
            InlineKeyboardButton(text=district, callback_data=DistrictCallbackFactory(district=district).pack()),
        )

    builder.row(create_back_button())

    return builder.as_markup()


def create_select_residential_complex_keyboard(
    residential_complexes: list[ResidentialComplex],
) -> InlineKeyboardMarkup:
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
