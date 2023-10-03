from .app_api import GenerateBotTokenView, SendMessageView, GetChatMessagesView

from django.urls import path

urlpatterns = [
    path('generate-token/', GenerateBotTokenView.as_view(), name="generate-token"),
    path('send-message/', SendMessageView.as_view(), name="send-message"),
    path('get-chat-messages/', GetChatMessagesView.as_view(), name="get-chat-messages"),
]
