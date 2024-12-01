import os

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

from config.settings.base import *

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent / "prod.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)

DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = os.getenv('SOCIAL_AUTH_TELEGRAM_BOT_TOKEN')
SOCIAL_AUTH_TELEGRAM_BOT_USERNAME = os.getenv("SOCIAL_AUTH_TELEGRAM_BOT_USERNAME")

TIME_ZONE = "Etc/GMT-3"
STATIC_ROOT = '/var/www/landing/'
CSRF_TRUSTED_ORIGINS = [
    'https://' + ALLOWED_HOSTS[0],
    'http://' + ALLOWED_HOSTS[0]
]
