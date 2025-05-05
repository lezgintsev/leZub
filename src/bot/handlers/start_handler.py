from aiogram import Router, types
from aiogram.filters import Command
from src.bot.keyboards.main_menu import get_main_menu

router = Router()

@router.message(Command("start"))
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
    
    # # Проверка на администратора (пример)
    # if message.from_user.id == YOUR_ADMIN_ID:  # Замените на ваш ID
    #     await message.answer(welcome_text, parse_mode="HTML", reply_markup=get_admin_menu())
    # else:
    #     await message.answer(welcome_text, parse_mode="HTML", reply_markup=get_main_menu())