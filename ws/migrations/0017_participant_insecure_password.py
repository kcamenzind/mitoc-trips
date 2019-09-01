# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-01 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('ws', '0016_archive_applications')]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='insecure_password',
            field=models.BooleanField(
                default=False, verbose_name='Password shown to be insecure'
            ),
        )
    ]
