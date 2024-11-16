import os
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs,async_sessionmaker,create_async_engine
from sqlalchemy import BigInteger,String,ForeignKey
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(url=os.getenv("SQL_ALCHEMY_URL"))
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs,DeclarativeBase):
    pass

class User(Base):
    __tablename__='users'
    
    id: Mapped[int]=mapped_column(primary_key = True,autoincrement=True)
    tg_id = mapped_column(BigInteger)
   
    
    
class PopQuestion(Base):
    __tablename__='pop_questions'
    
    id: Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    question: Mapped[str]=mapped_column(String(200))
    
class Answer(Base):
    __tablename__ = 'answers'
    
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    answer: Mapped[str] = mapped_column(String(300))
    question:Mapped[int]=mapped_column(ForeignKey('pop_questions.id'))
         
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)