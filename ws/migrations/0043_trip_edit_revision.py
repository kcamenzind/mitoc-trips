# Generated by Django 3.2.13 on 2022-05-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws', '0042_alter_trip_signups_open_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='edit_revision',
            field=models.PositiveIntegerField(
                default=0,
                help_text='An incremented integer, to avoid simultaneous edits to the trip.',
            ),
        ),
    ]
