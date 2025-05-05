from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.bot.config import load_config

config = load_config()

# Подключение к MySQL через aiomysql
DATABASE_URL = f"mysql+aiomysql://{config.db_user}:{config.db_password}@{config.db_host}/{config.db_name}"

# Движок
engine = create_async_engine(DATABASE_URL, echo=False)

# Сессия
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Базовый класс моделей
Base = declarative_base()
