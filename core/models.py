from django.db import models
from django.apps import apps

# Create your models here.
# 봄 축제 복붙입니다.
def image_upload_path(instance, filename): 
    # media/app이름 
    app_name = apps.get_containing_app_config(type(instance).__module__).name
    if app_name == 'booth':
        image_path = instance.booth.pk
    return f'{app_name}/{instance.booth.pk}/{filename}'

# 실제 테이블 생성 안되는 Abstract 모델입니다.
class Base_image(models.Model):
    image=models.ImageField(upload_to=image_upload_path, blank=True, null=True)

    class Meta:
        abstract = True
