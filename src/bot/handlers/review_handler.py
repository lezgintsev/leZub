from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from src.bot.database.db import async_session
from src.bot.database.models import Review

router = Router()

# Состояние для FSM
class ReviewStates(StatesGroup):
    waiting_for_text = State()

# Обработка кнопки "Оставить отзыв"
@router.message(F.text == "✏️ Оставить отзыв")
async def ask_for_review(message: types.Message, state: FSMContext):
    await message.answer(
        "✍️ Пожалуйста, напишите, что вам понравилось или не понравилось.\n\nНам очень важно ваше мнение!"
    )
    await state.set_state(ReviewStates.waiting_for_text)

# Приём текста отзыва и сохранение в БД
@router.message(ReviewStates.waiting_for_text)
async def receive_review(message: types.Message, state: FSMContext):
    user = message.from_user

    # Создаём объект отзыва
    review = Review(
        user_id=user.id,
        username=user.username,
        full_name=user.full_name,
        review_text=message.text
    )

    # Сохраняем в базу данных
    async with async_session() as session:
        session.add(review)
        await session.commit()

    # Ответ пользователю
    await message.answer("✅ Спасибо за ваш отзыв! Мы обязательно его учтём.")
    await state.clear()
