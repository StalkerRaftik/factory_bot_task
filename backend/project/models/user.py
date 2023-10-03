from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_bot_token = models.UUIDField(null=True, blank=True)

