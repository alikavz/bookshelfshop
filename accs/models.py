from django.db import models
from django.contrib.auth.models import AbstractUser


class Customizeuser(AbstractUser):
    sen = models.PositiveIntegerField(null=True, blank=True)

