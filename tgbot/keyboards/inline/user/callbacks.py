from aiogram.filters.callback_data import CallbackData


class DistrictCallbackFactory(CallbackData, prefix='district'):
    district: str


class ResidentialComplexCallbackFactory(CallbackData, prefix='residential_complex'):
    residential_complex_id: int


class HouseCallbackFactory(CallbackData, prefix='house'):
    house_id: int
