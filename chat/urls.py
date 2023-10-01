from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'chat'

# booth_router = routers.SimpleRouter(trailing_slash=False)
# booth_router.register('booths', BoothViewSet, basename='chat')


# urlpatterns = [
#     path('', include(booth_router.urls)),
# ]