from aiogram.filters.callback_data import CallbackData


class HouseCallbackFactory(CallbackData, prefix='house'):
    house_id: int
