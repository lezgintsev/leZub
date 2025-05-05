import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    TG_BOT_TOKEN: str
    
    class Config:
        env_file = ".env"

async def main():
    config = Config()
    
    # Новый способ инициализации бота в aiogram 3.7.0+
    bot = Bot(
        token=config.TG_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("🦷 Добро пожаловать в стоматологическую клинику!")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())