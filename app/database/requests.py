from sqlalchemy import select
from app.database.models import User, PopQuestion, Answer
from app.database.models import async_session


def connection(func):
    async def wrapper(*args,**kwargs):
         async with async_session() as session:
            return  await func(session,*args,**kwargs)
    return wrapper    
     
@connection
async def set_user(session,tg_id:int):    
    user = await session.scalar(select(User).where(User.tg_id == tg_id))        
    if not user:
        session.add(User(tg_id=tg_id))
        await session.commit()
        
@connection
async def get_questions(session):
    return await session.scalars(select(PopQuestion))

@connection
async def get_answer_by_question_id(session,question_id:int):
    return await session.scalar(select(Answer).where(Answer.question == question_id))
            
        
        
        