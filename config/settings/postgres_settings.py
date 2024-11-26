import os

from dotenv import load_dotenv

from config.settings.common_settings import *

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent / "prod.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)

DEBUG = False
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
TIME_ZONE = "Etc/GMT-3"
