import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage  # Добавили FSM-хранилище

from src.bot.config import load_config
from src.bot.handlers import (
    start_handler,
    review_handler,
    info_handler,
    contacts_handler
    
)

async def main():
    # Загружаем конфигурацию из .env
    config = load_config()

    # Инициализируем бота
    bot = Bot(
        token=config.tg_bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # FSM-хранилище (в памяти)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Подключаем все обработчики
    dp.include_router(start_handler.router)
    dp.include_router(info_handler.router)
    dp.include_router(contacts_handler.router)
    dp.include_router(review_handler.router)

    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
