from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from telegram.bot import create_bot_instance

from apps.core.models import Chat, Message

User = get_user_model()


def create_polling_bot():
    bot = create_bot_instance()

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        welcome_text = """Команды:
        /token - привязка пользователя к чату
        """

        bot.reply_to(message, welcome_text)

    @bot.message_handler(commands=['token'])
    def link_token(message):
        token = message.text.split(' ')[-1]
        try:
            user = User.objects.filter(telegram_bot_token=token).first()
        except ValidationError:
            user = None

        if not user:
            bot.reply_to(message, 'Пользователь не найден')
            return

        chat_id = message.chat.id
        chat, created = Chat.objects.get_or_create(user=user, chat_id=chat_id)
        if not created:
            chat.chat_id = chat_id
            chat.save()

        bot.reply_to(message, "Чат успешно связан с пользователем системы")

    @bot.message_handler(func=lambda message: True)
    def save_message(message):
        chat_id = message.chat.id
        chat = Chat.objects.filter(chat_id=chat_id).first()
        if not chat:
            return

        Message.objects.create(
            chat=chat,
            message_body=message.text,
            date=datetime.fromtimestamp(message.date).date(),
        )

    return bot
