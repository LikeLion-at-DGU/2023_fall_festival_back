from django.db import models
from core.models import Base_image

# Create your models here.
# 부스
class Booth(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    TYPE_CHOICES=(
        # 자유롭게 수정
        # ('주간부스','주간부스'),
        # ('야간부스','야간부스'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    operater = models.CharField(max_length=255)
    LOCATION_CHOICES=(
        # 자유롭게 수정하세요
        # ('이해랑예술극장','이해랑예술극장'),
        # ('사회과학관','사회과학관'),
        # ('혜화관','혜화관'),
        # ('혜화별관','혜화별관'),
        # ('명진관','명진관'),
        # ('팔정도','팔정도'),
        # ('원흥관 4층','원흥관 4층'),
        # ('만해광장','만해광장'),
        # ('학생회관','학생회관'),
        # ('학림관','학림관'),
    )
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    description = models.CharField(max_length=255)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    # 필요시 사용하는 필드와 함수
    # thumbnail = models.ImageField(null=True, blank=True)
    # during = models.DateTimeField(null=True, blank=True)
    # is_liked = models.BooleanField(null=True, blank=True, default=False)

    # def __str__(self):
    #     return self.name

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
# 이부분은 봄 축제 참고하였음. 수정 시 알려주세용
class Booth_image(Base_image):
    booth=models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='boothimages')
