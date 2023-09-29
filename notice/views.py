from django.shortcuts import render
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework import viewsets


class NotificationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    
    
# class PromotionViewSet(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     viewsets.GenericViewSet,
# ):
#     serializer_class = PromotionSerializer
#     queryset = Promotion.objects.all()


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        first_image = instance.promotionimages.first()
        print("---->"+first_image)
        if first_image:
            instance.thumbnail = first_image.image.url
            instance.save()