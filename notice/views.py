from django.shortcuts import render
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework import viewsets
from .paginations import NoticePagination, PromotePagination
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

# 공지 type 필터링
class NotificationFilter(filters.FilterSet):
    
    class Meta:
        model = Notification
        fields = ['type']


class NotificationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = [DjangoFilterBackend]
    filterset_class = NotificationFilter
    
    pagination_class = NoticePagination  
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return NotificationListSerializer
        return NotificationSerializer
    
    
    # 공지 게시물 첫번째 이미지를 썸네일로 지정
    def perform_create(self, serializer):
        instance = serializer.save()
        first_image = instance.notificationimages.first()
        if first_image:
            instance.thumbnail = first_image.image.url
            instance.save()
    


# 홍보 type 필터링
class PromotionFilter(filters.FilterSet):

    class Meta:
        model = Promotion
        fields = ['type']


class PromotionViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = [DjangoFilterBackend]
    filterset_class = PromotionFilter
    
    pagination_class = PromotePagination
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PromotionListSerializer
        return PromotionSerializer
    

    # 홍보 게시물 첫번째 이미지를 썸네일로 지정
    def perform_create(self, serializer):
        instance = serializer.save()
        first_image = instance.promotionimages.first()
        if first_image:
            instance.thumbnail = first_image.image.url
            instance.save()