from django.db import models

# Create your models here.
# 방명록
class Chat(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # min_length, max_length 10~100인데 프론트와 협의 후 변경
    content = models.TextField()
    ICON_CHOICES=(
        ('hip','hip'),
        ('festival','festival'),
        ('fire','fire'),
        ('heart','heart'),
        ('haapy','haapy'),
        ('best','best'),  
        ('cry','cry'),      
    )
    icon = models.CharField(
        max_length=10,
        choices=ICON_CHOICES,
        default='festival',
    )
    key=models.CharField(
        max_length=50,
        blank=True,
        editable=False
    )
    is_abused = models.BooleanField(default=False)