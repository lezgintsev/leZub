from pydantic_settings import BaseSettings

class Config(BaseSettings):
    tg_bot_token: str
    db_host: str
    db_user: str
    db_password: str
    db_name: str
    
    class Config:
        env_file = ".env"

def load_config() -> Config:
    return Config()