from django.contrib import admin

from .models import Picture, PictureAdmin

admin.site.register(Picture, PictureAdmin)
