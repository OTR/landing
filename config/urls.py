from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from landing_app.views.login import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("landing_app.urls", namespace="landing_app")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    re_path('^social/', include("social_django.urls", namespace='social')),
    re_path('^auth/', include("drf_social_oauth2.urls", namespace='drf')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
