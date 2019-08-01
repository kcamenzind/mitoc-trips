# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('ws', '0015_lotteryadjustment')]

    operations = [
        migrations.AddField(
            model_name='climbingleaderapplication',
            name='archived',
            field=models.BooleanField(
                default=False,
                help_text='Application should not be considered pending. Allows participant to submit another application if they desire.',
            ),
        ),
        migrations.AddField(
            model_name='hikingleaderapplication',
            name='archived',
            field=models.BooleanField(
                default=False,
                help_text='Application should not be considered pending. Allows participant to submit another application if they desire.',
            ),
        ),
        migrations.AddField(
            model_name='winterschoolleaderapplication',
            name='archived',
            field=models.BooleanField(
                default=False,
                help_text='Application should not be considered pending. Allows participant to submit another application if they desire.',
            ),
        ),
    ]