# Generated by Django 3.0.4 on 2020-03-16 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 11, 43, 17, 978291, tzinfo=utc)),
        ),
    ]
