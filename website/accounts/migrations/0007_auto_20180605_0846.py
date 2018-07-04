# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 08:46
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180605_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_details',
            name='avatar',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='avatar'),
        ),
    ]
