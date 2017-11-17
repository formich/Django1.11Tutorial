# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-15 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20171115_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
