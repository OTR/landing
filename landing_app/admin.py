from django.contrib import admin
from django.contrib.auth.models import Group
# from django_celery_beat.models import PeriodicTask, IntervalSchedule

from landing_app.models import AppUserModel


@admin.register(AppUserModel)
class AppUserModelAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


admin.site.unregister(Group)

# admin.site.register(PeriodicTask)
# admin.site.register(IntervalSchedule)
