# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0010_auto_20150705_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='notice',
            field=models.CharField(default=b'unpaid', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='paid',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
