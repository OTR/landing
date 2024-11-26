from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("landing_app.infra.urls", namespace="landing_app")),
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
