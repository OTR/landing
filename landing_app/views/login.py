from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework import routers, serializers, viewsets


class LoginView(TemplateView):
    template_name = "landing_app/login.html"
    content_type = 'text/html'

    extra_context = {
        "BOT_USERNAME": settings.SOCIAL_AUTH_TELEGRAM_BOT_USERNAME,
        "HOSTNAME": settings.ALLOWED_HOSTS[0]
    }

    def dispatch(self, request, *args, **kwargs):
        if request.path == "/login" and request.user.is_authenticated:
            return redirect('/profile')

        return super().dispatch(request, *args, **kwargs)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
