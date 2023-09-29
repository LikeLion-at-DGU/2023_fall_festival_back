from django.shortcuts import render
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework import viewsets
from .paginations import NoticePagination, PromotePagination

class NotificationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pagination_class = NoticePagination  
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    

class PromotionViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pagination_class = PromotePagination
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        first_image = instance.promotionimages.first()
        if first_image:
            instance.thumbnail = first_image.image.url
            instance.save()