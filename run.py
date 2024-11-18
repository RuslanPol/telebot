import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers.handlers import router as heandlers_router
from app.database.models import async_main

# Загрузка переменных окружения из файла .env
load_dotenv()
# Получение токена бота из переменной окружения
bot_token = os.getenv("BOT_TOKEN")

bot = Bot(token=bot_token)
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(heandlers_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")

# Инициализация бота
