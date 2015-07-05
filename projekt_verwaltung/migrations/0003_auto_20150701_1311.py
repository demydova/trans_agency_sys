# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0002_auto_20150629_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='invoice',
            field=models.CharField(default=b'invoice-0001_2015', max_length=30),
        ),
        migrations.AddField(
            model_name='project',
            name='notice',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='words_number',
            field=models.FloatField(default=0.0),
        ),
    ]
