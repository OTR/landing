from django.urls import path
from django.views.generic import TemplateView

import landing_app.apps

app_name = landing_app.apps.LandingAppConfig.name

urlpatterns = [
    path("login", TemplateView.as_view(template_name="landing_app/login.html", content_type='text/html')),
]
