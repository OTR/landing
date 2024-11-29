from django.views.generic import TemplateView
from rest_framework import routers, serializers, viewsets
from landing_app.models.user import User

class LoginView(TemplateView):
    template_name = "landing_app/login.html"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
