from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from apps.users.managers import UserManager

class User(AbstractUser):
    first_name = None
    last_name = None
    email = None

    phone = models.CharField(_("Phone"), max_length=15, unique=True)
    full_name = models.CharField(_("Full name"), max_length=100, null=True, blank=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()
