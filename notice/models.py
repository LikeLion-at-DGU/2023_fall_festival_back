from django.db import models
from core.models import *

# 공지
class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    TYPE_CHOICES = (
        # 카테고리
        ('축제','축제'),
        ('기타','기타'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

# 홍보
class Promotion(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    TYPE_CHOICES = (
        # 카테고리
        ('동아리','동아리'),
        ('학과','학과'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)



# 공지 이미지
class Notification_image(Base_image):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='notificationimages')
    image = models.ImageField(upload_to=notification_image_upload_path, blank=True, null=True)

# 홍보 이미지
class Promotion_image(Base_image):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='promotionimages')
    image = models.ImageField(upload_to=promotion_image_upload_path, blank=True, null=True)