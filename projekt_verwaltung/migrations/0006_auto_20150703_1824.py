# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0005_auto_20150703_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='paid',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.FloatField(default=0.0, editable=False),
        ),
    ]
