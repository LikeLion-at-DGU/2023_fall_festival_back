from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'chat'

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register('chat', ChatViewSet, basename='chat')

urlpatterns = [
    path('', include(default_router.urls)),
]