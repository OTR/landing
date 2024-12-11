from django.apps import AppConfig


class LandingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "landing_app"

    def ready(self) -> None:
        super().ready()
