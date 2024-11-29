from django.urls import path

import landing_app.apps
from landing_app.views.login import LoginView

app_name = landing_app.apps.LandingAppConfig.name

urlpatterns = [
    path("login", LoginView.as_view(), name="index"),
]
