import uuid

from django.contrib.auth import get_user_model
from rest_framework import serializers, permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    telegram_bot_token = serializers.UUIDField(read_only=True)

    class Meta:
        model = User
        fields = ('telegram_bot_token',)


class GenerateBotTokenView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        user.telegram_bot_token = uuid.uuid4()
        user.save()

        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
