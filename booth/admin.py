from django.contrib import admin
from .models import Booth, Booth_image, Booth_like

# admin.site.register(Booth)
admin.site.register(Booth_like)
# admin.site.register(Booth_image)

class BoothImageInline(admin.TabularInline):
    model = Booth_image
    extra = 5

@admin.register(Booth)
class NotificationAdmin(admin.ModelAdmin):
    inlines = [BoothImageInline]
