from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    MONGO_URI: str 
    BUS_DB_NAME: str 
 
    class Config:
        env_file = Path(__file__).resolve().parents[3] / ".env"
        env_file_encoding = "utf-8"

settings = Settings()
print("Loaded MONGO_URI:", settings.MONGO_URI)
