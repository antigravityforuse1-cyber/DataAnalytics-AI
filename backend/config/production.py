from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    environment: str = "development"
    debug: bool = True
    gemini_api_key: str = ""
    cors_origins: List[str] = ["http://localhost:3000", "*"]
    database_url: str = "sqlite:///./app.db"
    upload_dir: str = "./uploads"
    export_dir: str = "./exports"

    class Config:
        env_file = ".env"

settings = Settings()
