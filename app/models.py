from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.conf.global_settings import DATETIME_FORMAT


from django.contrib.auth.models import AbstractUser

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model

from django.conf import settings


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):

        # if not email:
        #     raise ValueError(_('The Email must be set'))
        # email = self.normalize_email(email)
        if 'email' in extra_fields:
            if not email:
                raise ValueError(_('The Email must be set'))
            email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    id = models.CharField(max_length=255, primary_key=True)
    timezone = models.CharField(max_length=255)
    username = models.CharField(
        max_length=255, unique=True, blank=False, null=False)

    email = models.EmailField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'password']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class activity(models.Model):
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
