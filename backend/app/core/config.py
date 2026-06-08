from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    # ========================
    # App
    # ========================
    APP_NAME: str = "AskMyDoc API"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # ========================
    # Database
    # ========================
    DATABASE_URL: str

    # ========================
    # Redis
    # ========================
    REDIS_URL: str = "redis://localhost:6379/0"

    # ========================
    # JWT
    # ========================
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # ========================
    # OAuth — Google
    # ========================
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    # ========================
    # OAuth — GitHub
    # ========================
    GITHUB_CLIENT_ID: str
    GITHUB_CLIENT_SECRET: str

    # ========================
    # OAuth — Facebook
    # ========================
    FACEBOOK_CLIENT_ID: str
    FACEBOOK_CLIENT_SECRET: str

    # ========================
    # OpenAI
    # ========================
    OPENAI_API_KEY: str
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"
    OPENAI_CHAT_MODEL: str = "gpt-4o-mini"

    # ========================
    # Cloudflare R2
    # ========================
    R2_ACCESS_KEY_ID: str
    R2_SECRET_ACCESS_KEY: str
    R2_BUCKET_NAME: str
    R2_ENDPOINT_URL: str

    # ========================
    # CORS
    # ========================
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    # ========================
    # Celery
    # ========================
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()