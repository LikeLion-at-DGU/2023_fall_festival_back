from django.contrib import admin
from .models import *

# 게시물 당 이미지 5개까지 업로드 가능
class NotificationImageInline(admin.TabularInline):
    model = Notification_image
    extra = 5

class PromotionImageInline(admin.TabularInline):
    model = Promotion_image
    extra = 5

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    inlines = [NotificationImageInline]

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    inlines = [PromotionImageInline]