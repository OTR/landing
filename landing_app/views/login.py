from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "landing_app/login.html"
