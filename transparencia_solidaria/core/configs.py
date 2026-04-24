# %%
import os
from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import declarative_base

load_dotenv()


class Settings(BaseSettings):
    DB_URL: str = f'postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@localhost:5432/startup'
    DBBaseModel: ClassVar = declarative_base()
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory='templates')
    MEDIA: Path = Path('media')

    model_config = SettingsConfigDict(
        case_sensitive=True,
        # opcional: carregar de .env
        # env_file = ".env",
        # env_file_encoding = "utf-8",
    )

settings: Settings = Settings()

if __name__ == '__main__':
    settings = Settings()
    print(f'User: {os.getenv("DB_USER")} | Psswrd: {os.getenv("DB_PASSWORD")}')
    print('pronto!')
