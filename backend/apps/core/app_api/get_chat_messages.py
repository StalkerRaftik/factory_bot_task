from rest_framework import generics, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from apps.core.models import Message, Chat


class GetChatMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ('id', 'date', 'chat', 'message_body')


class GetChatMessagesView(generics.ListAPIView):
    serializer_class = GetChatMessagesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        chat = Chat.objects.filter(user=user).first()

        if not chat:
            raise ValidationError('Chat not linked')
        return chat.messages.all()
