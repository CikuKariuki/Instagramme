# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapics', '0008_auto_20190522_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='profiles/'),
        ),
    ]