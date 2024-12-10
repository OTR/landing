import os

from dotenv import load_dotenv

from config.settings.base import *

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent / "prod.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)

DEBUG = True
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "0.0.0.0"
]
SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = os.getenv('SOCIAL_AUTH_TELEGRAM_BOT_TOKEN')
SOCIAL_AUTH_TELEGRAM_BOT_USERNAME = os.getenv("SOCIAL_AUTH_TELEGRAM_BOT_USERNAME")

TIME_ZONE = "Etc/GMT-3"
STATIC_ROOT = str(BASE_DIR / "staticfiles")
CSRF_TRUSTED_ORIGINS = [
    'https://' + ALLOWED_HOSTS[0],
    'http://' + ALLOWED_HOSTS[0]
]
#
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'UTC'
#
# INSTALLED_APPS += ['django_celery_beat']
