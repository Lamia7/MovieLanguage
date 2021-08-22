import os

from dotenv import load_dotenv, find_dotenv

from .base import *  # noqa: F401, F403


# Find .env file
load_dotenv(find_dotenv())

# ENV as development by default, check .env file if production
ENV = os.getenv("ENV")

ALLOWED_HOSTS = ["142.93.35.59"]

SECRET_KEY = os.getenv("SECRET_KEY", default="foo-key")

# SECURITY WARNING: don't run with debug turned on in production!
# False if ENV=prod, by default, ENV=development (True)
#DEBUG = False if ENV == "production" else True
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME", default=""),
        "USER": os.getenv("DB_USER", default=""),
        "PASSWORD": os.getenv("DB_PASSWORD", default=""),
        "HOST": os.getenv("HOST", default=""),
        "PORT": os.getenv("PORT", default=""),
    }
}

# Static files path for deployment
STATIC_ROOT = BASE_DIR / "staticfiles"
