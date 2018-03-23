# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ws', '0002_participant_profile_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='wimp',
            field=models.ForeignKey(blank=True, help_text='Ensures the trip returns safely. Can view trip itinerary, participant medical info.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wimp_trips', to='ws.Participant', verbose_name='WIMP'),
        ),
    ]
