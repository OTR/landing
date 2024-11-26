from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "landing_app/index.html"
