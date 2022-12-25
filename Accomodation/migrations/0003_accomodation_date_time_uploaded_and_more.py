# Generated by Django 4.1.4 on 2022-12-25 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accomodation', '0002_accomodation_image_1_accomodation_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodation',
            name='date_time_uploaded',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
