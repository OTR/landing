from django.contrib import admin
from django.contrib.auth.models import Group

from landing_app.infra.models import AppUserModel


@admin.register(AppUserModel)
class AppUserModelAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


admin.site.unregister(Group)
