from aiogram.fsm.state import State, StatesGroup


class CreateResidentialComplex(StatesGroup):
    district = State()
    title = State()


class DeleteResidentialComplex(StatesGroup):
    district = State()
    residential_complex_id = State()


class CreateHouse(StatesGroup):
    district = State()
    residential_complex = State()
    numbers = State()
    link_chat = State()
