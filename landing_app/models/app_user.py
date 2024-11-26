from django.db import models


class AppUserModel(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="First name",null=False, blank=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.first_name)
