# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 22:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20170607_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 7, 1, 25, 46, 766103)),
        ),
    ]
