from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    environment: str = "development"
    debug: bool = True
    gemini_api_key: str = ""
    cors_origins: str = "*"
    database_url: str = "sqlite:///./app.db"
    upload_dir: str = "./uploads"
    export_dir: str = "./exports"

    @property
    def get_cors_origins(self) -> list:
        # Ignore any literal brackets if they tried to input JSON anyway
        raw = self.cors_origins.replace('[', '').replace(']', '').replace('"', '').replace("'", "")
        if raw == "*":
            return ["*"]
        return [o.strip() for o in raw.split(",") if o.strip()]

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
