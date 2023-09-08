import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

env = load_dotenv(BASE_DIR / ".env")

SECRET_KEY = str(os.getenv("SECRET_KEY", default=""))

DEBUG = bool(os.getenv("DEBUG", default=False))

SQLALCHEMY_DATABASE_URI = str(
    os.getenv("SQLALCHEMY_DATABASE_URI", default="")
)
