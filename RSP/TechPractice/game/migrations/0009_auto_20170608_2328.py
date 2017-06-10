# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 20:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20170608_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 8, 23, 28, 14, 17903)),
        ),
        migrations.AlterField(
            model_name='player',
            name='joindate',
            field=models.DateField(default=datetime.datetime(2017, 6, 8, 20, 28, 14, 17903, tzinfo=utc)),
        ),
    ]
