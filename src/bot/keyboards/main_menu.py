from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="🦷 Записаться на прием")],
        [KeyboardButton(text="📅 Мои записи"), KeyboardButton(text="ℹ️ О клинике")],
        [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="✏️ Оставить отзыв")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_admin_menu() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="📊 Статистика")],
        [KeyboardButton(text="📝 Управление записями")],
        [KeyboardButton(text="📢 Рассылка")],
        [KeyboardButton(text="◀️ В главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
