# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 00:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_auto_20170609_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='bet1',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='bet2',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 9, 3, 36, 7, 605670)),
        ),
    ]