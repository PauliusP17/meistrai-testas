# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meistrai_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='pictures', verbose_name='Image'),
        ),
    ]
