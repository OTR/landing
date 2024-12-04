from typing import Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView
from social_django.models import UserSocialAuth


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "landing_app/profile.html"
    content_type = 'text/html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user: User = self.request.user
        if hasattr(user, 'social_auth') and user.social_auth.all().exists():
            social_user: UserSocialAuth = user.social_auth.all()[0]
            social_auth_provider: str = social_user.provider
            extra = social_user.extra_data
            social_auth_username: Optional[str] = None
            if ('username' in extra
                    and isinstance(extra['username'], list)
                    and extra['username']):
                social_auth_username = extra['username'][0]
            social_auth_first_name: str = extra['first_name'][0]
            social_auth_id: str = extra['id'][0]
            context.update({
                "SOCIAL_AUTH_PROVIDER": social_auth_provider,
                "SOCIAL_AUTH_ID": social_auth_id,
                "SOCIAL_AUTH_FIRST_NAME": social_auth_first_name,
                "SOCIAL_AUTH_USERNAME": social_auth_username
            })
        else:
            context.update({"DJANGO_USER": user.username})

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.path == "/profile" and not request.user.is_authenticated:
            return redirect('/login')

        return super().dispatch(request, *args, **kwargs)
