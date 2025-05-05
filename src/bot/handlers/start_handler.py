from aiogram import Router, types
from aiogram.filters import CommandStart

from src.bot.keyboards.main_menu import get_main_menu, get_admin_menu
from src.bot.config import load_config

router = Router()
config = load_config()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = """
    🏥 <b>Добро пожаловать в стоматологию "Улыбк"!</b> 🦷

    Мы предлагаем полный спектр стоматологических услуг:
    • Лечение зубов
    • Отбеливание
    • Имплантация
    • Ортодонтия
    • Детская стоматология

    Выберите действие:
    """

    # Получаем список админов из строки и преобразуем в числа
    admin_ids = [int(x.strip()) for x in config.admin_ids.split(",")]

    # Проверяем, является ли пользователь админом
    if message.from_user.id in admin_ids:
        await message.answer(welcome_text, reply_markup=get_admin_menu())
    else:
        await message.answer(welcome_text, reply_markup=get_main_menu())
