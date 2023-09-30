from django.db import models

# Create your models here.
# 봄 축제 복붙입니다.
def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

def booth_image_upload_path(instance, filename):
    return f'booth/{instance.booth.id}/{filename}'

def notification_image_upload_path(instance, filename):
    return f'notification/{instance.notification.id}/{filename}'

def promotion_image_upload_path(instance, filename):
    return f'promotion/{instance.promotion.id}/{filename}'



# 실제 테이블 생성 안되는 Abstract 모델입니다.
class Base_image(models.Model):
    image=models.ImageField(upload_to=image_upload_path, blank=True, null=True)

    class Meta:
        abstract = True
