from django.db import models
from core.models import *

# Create your models here.
# 공지
class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    # max_length 협의 후 수정
    title = models.CharField(max_length=255)
    # text, char 협의 후 수정 
    content = models.TextField()
    # 세부사항 수정 가능
    created_at = models.DateTimeField(null=True, blank=True)
    TYPE_CHOICES = (
        # 카테고리
        ('축제','축제'),
        ('기타','기타'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    # 필요시 추가하세요
    # thumbnail = models.ImageField()

# 홍보
class Promotion(models.Model):
    id = models.IntegerField(primary_key=True)
    # max_length 협의 후 수정
    title = models.CharField(max_length=255)
    # text필드인지, char필드인지 협의 후 수정 
    content = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    TYPE_CHOICES = (
        # 카테고리
        ('동아리','동아리'),
        ('학과','학과'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    # 필요시 추가하세요
    # thumbnail = models.ImageField(upload_to='promotion_thumbnails/', blank=True, null=True)



# 공지, 홍보 이미지
class Notification_image(Base_image):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='notificationimages')
    image = models.ImageField(upload_to=notification_image_upload_path, blank=True, null=True)


class Promotion_image(Base_image):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='promotionimages')
    image = models.ImageField(upload_to=promotion_image_upload_path, blank=True, null=True)