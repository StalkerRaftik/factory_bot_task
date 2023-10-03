from datetime import datetime

from rest_framework import generics, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from apps.core.models import Message, Chat
from telegram.bot import create_bot_instance


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ('id', 'date', 'chat',)


class SendMessageView(generics.CreateAPIView):
    serializer_class = SendMessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        chat = Chat.objects.filter(user=user).first()
        message = serializer.validated_data['message_body']
        if not chat:
            raise ValidationError("Chat not found")

        bot = create_bot_instance()
        message = bot.send_message(chat.chat_id, message)

        serializer.save(chat=chat, date=datetime.fromtimestamp(message.date).date())
