from aiogram import F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from sqlalchemy.testing import assert_raises_message
from app.ai.generators import generate
from aiogram.fsm.context import FSMContext
from app.states.work_states import Work
from aiogram.types import ReplyKeyboardRemove

import app.keyboards.keyboards as kb
import app.database.requests as requests

router = Router()
@router.message(CommandStart())
async def start_command(message: Message):
    await requests.set_user(message.from_user.id)
    await message.answer(
        f"Hello! {message.from_user.first_name}" ,     
        reply_markup=await kb.inline_question(kb.questions)
    )   

    
@router.message(Work.process)
async def stop(message:Message):
     await message.answer(f"{message.from_user.first_name}, подождите, ваше сообщение генерируется...")   
    
    
@router.callback_query(F.data == 'consultation') 
async def ai(callback: CallbackQuery,state:FSMContext):
    await state.set_state(Work.process)
    res = await generate(callback.message.text)
    await callback.message.answer(f"{res.choices[0].message.content}\n\n" 
                                  f"To access the main menu, select the /start command")
    await state.clear()
    
    
@router.message() 
async def ai(message:Message,state:FSMContext):
    await state.set_state(Work.process)
    res = await generate(message.text)
    await message.answer(res.choices[0].message.content)
    await state.clear()
        

@router.callback_query(F.data == 'to_menu')
async def faq(callback: CallbackQuery):
    await callback.answer('Вы хотите вернуться в меню')
    await callback.message.answer(
        f"Hello! {callback.from_user.first_name}" ,     
        reply_markup=await kb.inline_question(kb.questions))


@router.callback_query(F.data == 'frequently asked questions')
async def faq(callback: CallbackQuery):
    await callback.answer('Выбраны часто задаваемые вопросы')
    await callback.message.edit_text('ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ',
                                     reply_markup=await kb.inline_question_db())


@router.callback_query(F.data.startswith('question_'))
async def ans(callback: CallbackQuery):
    await callback.answer('Получите самый правильный ответ')
    question_id = callback.data.split('_')[1]
    answer = await requests.get_answer_by_question_id(question_id)
    if answer:
        await callback.message.answer(f'ОTBET:',
                                      reply_markup=await kb.inline_answer_db(question_id))
    else:
        await callback.message.answer("Извините, ответ не найден.",
                                      reply_markup=await kb.inline_answer_db(question_id))
    await callback.answer() 
    
   