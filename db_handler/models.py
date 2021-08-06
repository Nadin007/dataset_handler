from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class ShopsDB(models.Model):
    date = models.DateTimeField(auto_now=True)
    shop = models.TextField(max_length=100)
    country = models.TextField(max_length=10)
    visitors = models.IntegerField()
    earnings = models.IntegerField()

    def __str__(self):
        return f"{self.shop} based {self.country}"
