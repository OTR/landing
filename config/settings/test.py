from dotenv import load_dotenv

from config.settings.base import *

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent / "prod.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]
TIME_ZONE = "Etc/GMT-3"
STATIC_ROOT = str(BASE_DIR / "staticfiles")
