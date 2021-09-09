import os

from dotenv.main import find_dotenv
# from dotenv import load_dotenv, find_dotenv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


from .base import *  # noqa: F401, F403


# Find .env file
# load_dotenv(find_dotenv())
find_dotenv()

# ENV as development by default, check .env file if production
ENV = os.getenv("ENV")

ALLOWED_HOSTS = ["142.93.35.59", "movielanguage.lamiaweb.fr"]

# SECRET_KEY = os.getenv("SECRET_KEY", default="foo-key")

# SECURITY WARNING: don't run with debug turned on in production!
# False if ENV=prod, by default, ENV=development (True)
# DEBUG = False if ENV == "production" else True
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

# Sentry configuration
sentry_sdk.init(
    dsn=os.getenv("SENTRY"),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)