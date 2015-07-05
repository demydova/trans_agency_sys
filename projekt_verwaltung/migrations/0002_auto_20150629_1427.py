# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.date(2015, 6, 29)),
        ),
        migrations.AddField(
            model_name='project',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='project',
            name='src_language',
            field=models.CharField(default=b'German', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.date(2015, 6, 29), editable=False),
        ),
        migrations.AddField(
            model_name='project',
            name='target_language',
            field=models.CharField(default=b'Russian', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='word_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='words_number',
            field=models.IntegerField(default=0.0),
        ),
    ]
