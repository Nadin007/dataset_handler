from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Return the short name for the user
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class ShopsDB(models.Model):
    date = models.DateTimeField(auto_now=True)
    shop = models.TextField(max_length=100)
    country = models.TextField(max_length=10)
    visitors = models.IntegerField()
    earnings = models.IntegerField()

    def __str__(self):
        return f"{self.shop} based {self.country}"
