from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "monitoring-platform"
    storage: Literal["memory", "mongo"] = "mongo"
    mongo_url: str = "mongodb://localhost:27017"
    mongo_db: str = "monitoring"


settings = Settings()
