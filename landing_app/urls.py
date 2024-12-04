from django.urls import path
import landing_app.apps
from landing_app.views.login import LoginView
from landing_app.views.profile import ProfileView

app_name = landing_app.apps.LandingAppConfig.name

urlpatterns = [
    path("login", LoginView.as_view()),
    path("profile", ProfileView.as_view())
]
