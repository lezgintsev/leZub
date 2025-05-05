from sqlalchemy import Column, Integer, BigInteger, String, Text, DateTime, func
from src.bot.database.db import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    username = Column(String(255))
    full_name = Column(String(255))
    review_text = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())