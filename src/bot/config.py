from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    tg_bot_token: str
    db_host: str
    db_user: str
    db_password: str
    db_name: str
    admin_ids: str  # строка с ID через запятую

    class Config:
        env_file = ".env"
        extra = "forbid"  # запрещаем лишние поля (можно убрать если нужно)

def load_config() -> Settings:
    return Settings()
