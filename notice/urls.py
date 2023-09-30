from django.urls import include, path
from rest_framework import routers

from .views import NotificationViewSet, PromotionViewSet

default_notice_router = routers.SimpleRouter(trailing_slash=False)
default_notice_router.register("notification", NotificationViewSet, basename="notification")

default_promote_router = routers.SimpleRouter(trailing_slash=False)
default_promote_router.register("promotion", PromotionViewSet, basename="promotions")

urlpatterns = [
    path("", include(default_notice_router.urls)),
    path("", include(default_promote_router.urls)),
]