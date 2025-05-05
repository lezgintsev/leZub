from aiogram import Router, types

router = Router()

@router.message()
async def handle_buttons(message: types.Message):
    if message.text == "ℹ️ О клинике":
        await message.answer(
            text="""
<b>🦷 О нашей клинике "Улыбк"</b>

Наша стоматологическая клиника предлагает:
• Современное оборудование
• Опытных специалистов
• Индивидуальный подход к каждому пациенту

📍 Адрес: г. Москва, ул. Зубная, д. 1
🕘 Время работы: Пн–Сб с 9:00 до 20:00
📞 Телефон: +7 (999) 123-45-67
""",
            parse_mode="HTML"
        )
