# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0012_auto_20150705_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='paid',
            field=models.CharField(default=0.0, max_length=100, blank=True),
        ),
    ]
