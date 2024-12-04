from django.apps import AppConfig


class LandingAppConfig(AppConfig):
    name = "landing_app"

    def ready(self) -> None:
        super().ready()
