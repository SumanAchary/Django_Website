# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_users_details_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_details',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]