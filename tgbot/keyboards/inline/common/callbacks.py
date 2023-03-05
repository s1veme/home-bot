from aiogram.filters.callback_data import CallbackData


class MenuCallbackFactory(CallbackData, prefix='menu'):
    action: str


class DistrictCallbackFactory(CallbackData, prefix='district'):
    district: str


class ResidentialComplexCallbackFactory(CallbackData, prefix='residential_complex'):
    residential_complex_id: int
