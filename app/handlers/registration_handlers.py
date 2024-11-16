from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from app.states.registration_states import Registration
from app.keyboards.any_keyboards import request_contact_keyboard
import re

router = Router()


def is_valid_phone(phone: str) -> bool:
    # Пример регулярного выражения для проверки номера телефона
    # Здесь проверяем, что номер начинается с +7 или 8 и имеет длину 11 символов
    pattern = r'^(\+7|8)[0-9]{10}$'
    return re.match(pattern, phone) is not None


@router.message(F.text.lower()=='registration')
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer('Введите имя ')


@router.message(Registration.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.phone)
    await message.answer('Введите номер телефона',
                         reply_markup=await request_contact_keyboard())


@router.message(Registration.phone, F.text.func(is_valid_phone))
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо Вы зарегистрировались.'
                         f'\n Имя:{data["name"]} \n'
                         f'Телефон: {data["phone"]}')
    await state.clear()


@router.message(Registration.phone)
async def invalid_phone(message: Message):
    await message.answer(
        'Некорректный номер телефона. Пожалуйста,'
        ' введите номер в формате +7XXXXXXXXXX или 8XXXXXXXXXX')
