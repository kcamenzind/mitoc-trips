# Generated by Django 3.2.16 on 2022-10-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws', '0048_ws_application_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_type',
            field=models.CharField(
                choices=[
                    (
                        'Biking',
                        [
                            ('biking_road', 'Road biking'),
                            ('biking_mountain', 'Mountain biking'),
                        ],
                    ),
                    (
                        'Boating',
                        [
                            ('boating_canoeing', 'Canoeing'),
                            ('boating_kayaking', 'Kayaking'),
                            ('boating_kayaking_sea', 'Sea kayaking'),
                            ('boating_surfing', 'Surfing'),
                        ],
                    ),
                    (
                        'Climbing',
                        [
                            ('climbing_bouldering', 'Bouldering'),
                            ('climbing_gym', 'Gym climbing'),
                            ('climbing_ice', 'Ice climbing'),
                            ('climbing_sport', 'Sport climbing, top rope'),
                            ('climbing_trad', 'Trad climbing'),
                        ],
                    ),
                    (
                        'Hiking',
                        [
                            ('hiking_hiking', 'Hiking'),
                            ('hiking_trail_running', 'Trail running'),
                        ],
                    ),
                    (
                        'Skiing',
                        [
                            ('skiing_bc', 'Backcountry skiing'),
                            ('skiing_xc', 'Cross-country skiing'),
                            ('skiing_resort', 'Resort skiing'),
                        ],
                    ),
                    (
                        'Miscellaneous',
                        [
                            ('ice_skating', 'Ice skating'),
                            ('ultimate', 'Ultimate'),
                            ('yoga', 'Yoga'),
                        ],
                    ),
                    (
                        'Other, N/A',
                        [('none', 'None, or not applicable'), ('other', 'Other')],
                    ),
                ],
                max_length=255,
            ),
        ),
    ]
