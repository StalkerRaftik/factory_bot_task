from django.db import models


class Message(models.Model):
    chat = models.ForeignKey('core.Chat', on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    date = models.DateField()
