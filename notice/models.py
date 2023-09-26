from django.db import models
from core.models import Base_image

# Create your models here.
# 공지
class Notification(models.Model):
    id = models.BigIntegerField(primary_key=True)
    # max_length 협의 후 수정
    title = models.CharField(max_length=255)
    # text, char 협의 후 수정 
    content = models.CharField()
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
    id = models.BigIntegerField(primary_key=True)
    # max_length 협의 후 수정
    title = models.CharField(max_length=255)
    # text필드인지, char필드인지 협의 후 수정 
    content = models.CharField()
    created_at = models.DateTimeField(null=True, blank=True)
    TYPE_CHOICES = (
        # 카테고리
        ('동아리','동아리'),
        ('학과','학과'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    # 필요시 추가하세요
    # thumbnail = models.ImageField()

# 공지, 홍보 이미지
# 이부분은 봄 축제 참고하였음. 수정 시 알려주세용
class Notification_image(Base_image):
    notification=models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='notificationimages')

# 이부분은 봄 축제 참고하였음. 수정 시 알려주세용
class Promotion_image(Base_image):
    promotion=models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='promotionimages')