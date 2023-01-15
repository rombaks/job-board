import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    PG_USER: Optional[str] = os.getenv("POSTGRES_USER")
    PG_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    PG_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    PG_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    PG_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = (
        f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_SERVER}:{PG_PORT}/{PG_DB}"
    )


settings = Settings()
