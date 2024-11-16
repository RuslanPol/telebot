from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_questions, get_answer_by_question_id



questions = {
    'Хотите получить консультацию': 'consultation',
    'Часто задаваемые вопросы': 'frequently asked questions'   
}


async def inline_question(ques):
    inline_keyboard = InlineKeyboardBuilder()
    for value, key in ques.items():
        inline_keyboard.add(InlineKeyboardButton(text=value,
                                                 callback_data=key))
    return inline_keyboard.adjust(1).as_markup()  # adjust(2)- количество кнопок в строке


# вывод популярных вопросов
async def inline_question_db():
    all_questions = await get_questions()
    inline_keyboard = InlineKeyboardBuilder()
    for question in all_questions:
        inline_keyboard.add(InlineKeyboardButton(text=question.question,
                                                 callback_data=f'question_{question.id}'))
    inline_keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_menu'))
    return inline_keyboard.adjust(1).as_markup()
 
 
async def inline_answer_db(question_id):
    answer = await get_answer_by_question_id(question_id)
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.add(InlineKeyboardButton(text=answer.answer,
                                                 callback_data=f'answer_{answer.id}'))
    inline_keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_menu'))
    return inline_keyboard.adjust(1).as_markup()





