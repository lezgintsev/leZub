from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text == "📞 Контакты")
async def handle_contacts(message: types.Message):
    await message.answer(
        text="""
<b>📞 Контактная информация</b>

🏥 <b>Клиника «ЛеЗуб»</b>  
📍 Адрес: г. Санкт-Петербург, Комендантский проспект, д. 62  
📞 Телефон: +7 982-177-17-42  
✉️ Почта: lezub32@mail.ru  
🌐 Сайт: https://lezub.ru  
📱 Telegram: @lezub_clinic  
📸 Instagram: @lezub_clinic
""",
        parse_mode="HTML"
    )
