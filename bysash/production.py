from pathlib import Path
import os.path
import os
from dotenv import load_dotenv
from decouple import config
from .base import *
BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ["bysash.co", "www.bysash.co","188.121.121.229"]
DEBUG = False,

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

ALLOWED_HOSTS = [
    "bysash.co",
    "www.bysash.co",
]

CSRF_TRUSTED_ORIGINS = [
    "https://bysash.co",
    "https://www.bysash.co",
]

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True