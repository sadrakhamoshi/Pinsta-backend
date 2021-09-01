from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(blank=True, null=True)
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        db_table = 'users'
