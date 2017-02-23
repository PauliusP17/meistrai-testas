import os
from django.contrib import admin
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Picture(models.Model):
    image = models.ImageField('Image', upload_to=os.path.join('pictures'))
    image_thumb = ImageSpecField(
        # upload_to=os.path.join('pictures/thumbnails'),
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='PNG',
        options={'quality': 80})
    title = models.CharField('Title', max_length=100)
    comment = models.CharField('Comment', max_length=400)


class PictureAdmin(admin.ModelAdmin):
    exclude = ('image_thumb',)

