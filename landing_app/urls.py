from django.urls import path

import landing_app.apps
from landing_app.views import IndexView

app_name = landing_app.apps.LandingAppConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
