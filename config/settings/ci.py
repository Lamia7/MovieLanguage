import os

# from dotenv import load_dotenv, find_dotenv

from .base import *  # noqa: F401, F403


GITHUB_WORKFLOW = os.environ.get("GITHUB_WORKFLOW")

# ENV as development by default, check .env file if production
ENV = os.getenv("ENV")


# load_dotenv(find_dotenv(filename=".env-local")) ?

SECRET_KEY = os.getenv("SECRET_KEY", default="foo-key")

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

# SECURITY WARNING: don't run with debug turned on in production!
# False if ENV=prod, by default, ENV=development (True)
DEBUG = False if ENV == "production" else True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

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

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
