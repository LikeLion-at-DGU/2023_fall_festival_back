from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'chat'

chat_router = routers.SimpleRouter(trailing_slash=False)
chat_router.register('chat', ChatViewSet, basename='chat')

urlpatterns = [
    path('', include(chat_router.urls)),
]