# Generated by Django 4.1 on 2022-11-23 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0045_series_awaypreviousseries_series_homepreviousseries_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='points_potential',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 15, 10, 20, 242962), null=True),
        ),
    ]
