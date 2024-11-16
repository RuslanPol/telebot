from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_questions, get_answer_by_question_id

main_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='registration')],
              [KeyboardButton(text='questions')],
              [ KeyboardButton(text='get contact')              ,
               KeyboardButton(text='exit')]],
    resize_keyboard=True,
    input_field_placeholder='Выбрать пункт меню')

settings_menu = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text='YouTube',
            url=
            'https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4'
        )
    ],
        [
            InlineKeyboardButton(text='Change language',
                                 callback_data='change_language')
        ]])

async def request_contact_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Отправить контакт", request_contact=True)]
        ],
        resize_keyboard=True
    )
    return keyboard