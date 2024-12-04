import os

from dotenv import load_dotenv
import sentry_sdk

from config.settings.base import *

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent / "prod.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)

DEBUG = False
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',')
SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = os.getenv('SOCIAL_AUTH_TELEGRAM_BOT_TOKEN')
SOCIAL_AUTH_TELEGRAM_BOT_USERNAME = os.getenv("SOCIAL_AUTH_TELEGRAM_BOT_USERNAME")

TIME_ZONE = "Etc/GMT-3"
STATIC_ROOT = '/var/www/landing/'
CSRF_TRUSTED_ORIGINS = [
    'https://' + ALLOWED_HOSTS[0],
    'http://' + ALLOWED_HOSTS[0]
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'config.social_auth_pipelines.log_associated_user',  # Custom step
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SENTRY_DSN = os.getenv("SENTRY_DSN")

sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
    _experiments={"continuous_profiling_auto_start": True},
)
