from django.db import models

# Create your models here.
class Booth(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    TYPE_CHOICES=(
        ('주간부스','주간부스'),
        ('야간부스','야간부스'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    operater = models.CharField(max_length=255)
    LOCATION_CHOICES=(
        ('이해랑예술극장','이해랑예술극장'),
        ('사회과학관','사회과학관'),
        ('혜화관','혜화관'),
        ('혜화별관','혜화별관'),
        ('명진관','명진관'),
        ('팔정도','팔정도'),
        ('원흥관 4층','원흥관 4층'),
        ('만해광장','만해광장'),
        ('학생회관','학생회관'),
        ('학림관','학림관'),
    )
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    description = models.CharField()
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    # 필요시 사용하기
    # thumbnail = models.ImageField(null=True, blank=True)
    # during = models.DateTimeField(null=True, blank=True)
    # is_liked = models.BooleanField(null=True, blank=True, default=False)

    # def __str__(self):
    #     return self.name

class Booth_like(models.Model):
    booth=models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='likes')
    key=models.CharField(
        max_length=10,
        blank=True,
        editable=False
    )
    
    def __str__(self):
        return f'{self.booth}/{self.key}'

class Booth_image(models.Model):
    booth=models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='boothimages')
