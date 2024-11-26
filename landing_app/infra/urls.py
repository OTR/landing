from django.urls import path

import landing_app.infra.apps
from landing_app.infra.views import IndexView

app_name = landing_app.infra.apps.LandingAppConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
