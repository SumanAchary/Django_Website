# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180605_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_details',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]