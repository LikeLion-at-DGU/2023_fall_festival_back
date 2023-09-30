from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Notification)
# admin.site.register(Notification_image)

# admin.site.register(Promotion)
# admin.site.register(Promotion_image)


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