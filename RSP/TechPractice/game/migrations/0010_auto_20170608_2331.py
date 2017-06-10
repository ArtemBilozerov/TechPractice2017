# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 20:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20170608_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='time',
            field=models.DateTimeField(default=datetime.date(2017, 6, 8)),
        ),
        migrations.AlterField(
            model_name='player',
            name='joindate',
            field=models.DateField(default=datetime.datetime(2017, 6, 8, 20, 31, 56, 17910, tzinfo=utc)),
        ),
    ]