
from aiogram import F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message, CallbackQuery


import app.keyboards.any_keyboards as akb
import app.keyboards.keyboards as kb
import app.database.requests as requests

router = Router()

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        f"Hello! {message.from_user.first_name}, This is help command.",
        reply_markup=akb.settings_menu)


@router.message(Command('questions'))
async def standart_command(message: Message):
    await message.answer(
        f"Hello! {message.from_user.first_name}",  
        reply_markup=await kb.inline_question(kb.questions))


@router.message(F.text.lower() == 'how are you')
async def how_are_you(message: Message):
    await message.answer('I am fine, thank you!')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id} \n'
                         f'{message.from_user.first_name}, here is your photo')


@router.message(Command('get_photo'))
async def get_photo_command(message: Message):
    await message.answer_photo(
        photo=
        'AgACAgIAAxkBAANdZx-jsJPx6vbazJjB0g5krUwZq6cAAs_hMRubBflImpZJjjz6-1oBAAMCAAN5AAM2BA'
    )


@router.message(F.text.lower() == 'get contact')
async def request_contact(message: Message):
    await message.answer(
        "Пожалуйста, отправьте свой контакт:",
        reply_markup=await akb.request_contact_keyboard()

    )


@router.message(F.contact)
async def handle_contact(message: Message):
    phone_number = message.contact.phone_number
    await message.answer(
        f"Спасибо! Ваш номер телефона: {phone_number}",
        reply_markup=akb.main_menu
    )