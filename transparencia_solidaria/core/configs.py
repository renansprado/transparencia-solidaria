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
    DB_URL: str = f'postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST", "localhost")}:{os.getenv("DB_PORT", "5432")}/{os.getenv("DB_NAME", "transparencia_solidaria")}'
    DBBaseModel: ClassVar = declarative_base()
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory='templates')
    MEDIA: Path = Path('media')

    model_config = SettingsConfigDict(
        case_sensitive=True,
    )

settings: Settings = Settings()
