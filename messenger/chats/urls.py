from django.urls import path
from chats.views import *

urlpatterns = [
    path('get_chats/', get_chats),
    path('create_chat/', create_chat),
    path('', chat_app),
    path('chat_messages/', get_chat_messages),
    path('send_message/', send_message),
]