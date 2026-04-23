from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AutoMind Intelligence Platform"
    api_prefix: str = "/api"
    debug: bool = False
    google_api_key: str = ""
    google_text_model: str = "gemini-2.0-flash"
    google_image_model: str = "imagen-3.0-generate-002"
    groq_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"
    chroma_persist_dir: str = "./database/chroma"
    cors_origins: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
