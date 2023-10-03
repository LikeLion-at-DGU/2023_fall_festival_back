from django.db import models
from core.models import *

# 부스
class Booth(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    TYPE_CHOICES=(
        ('주간부스','주간부스'),
        ('야간부스','야간부스'),
        ('기타부스', '기타부스'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    operater = models.CharField(max_length=255)
    LOCATION_CHOICES=(
        ('사회과학관','사회과학관'),
        ('혜화관','혜화관'),
        ('팔정도','팔정도'),
        ('원흥관','원흥관'),
        ('만해광장','만해광장'),
        ('학생회관','학생회관'),
        ('학림관','학림관'),
    )
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    description = models.CharField(max_length=255)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    insta_url = models.URLField(default="http://www.instagram.com/your_username/")

    def __str__(self):
        return self.name

# 부스 좋아요
class Booth_like(models.Model):
    booth=models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='likes')
    key=models.CharField(
        max_length=10,
        blank=True,
        editable=False
    )
    
    def __str__(self):
        return f'{self.booth}/{self.key}'

# 부스 이미지
class Booth_image(Base_image):
    booth=models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='boothimages')
    image = models.ImageField(upload_to=booth_image_upload_path, blank=True, null=True)