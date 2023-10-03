from telebot import TeleBot
from django.conf import settings


def create_bot_instance():
    token = settings.TELEGRAM_TOKEN
    return TeleBot(token, parse_mode=None)
