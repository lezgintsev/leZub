import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.bot.config import load_config
from src.bot.handlers import start_handler
from src.bot.handlers import info_handler

async def main():
    # Загружаем конфиг из .env
    config = load_config()

    # Инициализируем бота
    bot = Bot(
        token=config.tg_bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # Создаём диспетчер
    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(start_handler.router)
    dp.include_router(info_handler.router)

    # Запускаем polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
