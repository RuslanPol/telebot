from app.database.models import async_session
from app.database.models import User,PopQuestion,Answer
from sqlalchemy import select

async def set_user(tg_id:int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_questions():
    async with async_session() as session:
        return await session.scalars(select(PopQuestion))

async def get_answer_by_question_id(question_id:int):
    async with async_session() as session:
        return await session.scalar(select(Answer).where(Answer.question == question_id))
            
        
        
        