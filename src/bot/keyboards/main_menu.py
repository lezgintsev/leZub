from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu() -> ReplyKeyboardMarkup:
    """
    Создает главное меню для пользователя
    """
    buttons = [
        [KeyboardButton(text="🦷 Записаться на прием")],
        [KeyboardButton(text="📅 Мои записи"), KeyboardButton(text="ℹ️ О клинике")],
        [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="✏️ Оставить отзыв")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_admin_menu() -> ReplyKeyboardMarkup:
    """
    Меню для администратора
    """
    buttons = [
        [KeyboardButton(text="📊 Статистика")],
        [KeyboardButton(text="📝 Управление записями")],
        [KeyboardButton(text="📢 Рассылка")],
        [KeyboardButton(text="◀️ В главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)