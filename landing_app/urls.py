from django.urls import path

import landing_app.apps
from landing_app.views.index import serve_html_file

app_name = landing_app.apps.LandingAppConfig.name

urlpatterns = [
    path("", serve_html_file, name="index"),
]
