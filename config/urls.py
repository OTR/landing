from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from landing_app.views.login import router

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        "login2",
        TemplateView.as_view(
            template_name="landing_app/login.html", content_type='text/html',
        ),
    ),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("landing_app.urls", namespace="landing_app")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
