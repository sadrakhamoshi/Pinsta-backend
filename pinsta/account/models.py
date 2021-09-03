import os

from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


def image_path_generator(instance, filename):
    type = filename.split('.')[-1]
    new_filename = '{}.{}'.format(uuid4().hex, type)
    return os.path.join('pictures/', new_filename)


class User(AbstractUser):
    avatar = models.ImageField(upload_to=image_path_generator, blank=True, null=True)
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        db_table = 'users'
