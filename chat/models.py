from django.db import models

# Create your models here.
# 방명록
class Chat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # min_length, max_length 10~100인데 프론트와 협의 후 변경
    content = models.CharField(max_length=100)
    key=models.CharField(
        max_length=10,
        blank=True,
        editable=False
    )
    
    def __str__(self):
        return f'{self.booth}/{self.key}'