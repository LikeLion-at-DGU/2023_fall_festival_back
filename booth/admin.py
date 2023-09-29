from django.contrib import admin
from .models import Booth, Booth_image, Booth_like

admin.site.register(Booth)
admin.site.register(Booth_like)
admin.site.register(Booth_image)