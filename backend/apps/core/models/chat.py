from django.db import models


class Chat(models.Model):
    user = models.OneToOneField('project.User', on_delete=models.CASCADE)
    chat_id = models.BigIntegerField(unique=True)
