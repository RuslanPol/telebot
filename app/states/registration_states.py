from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    name = State()
    phone = State()