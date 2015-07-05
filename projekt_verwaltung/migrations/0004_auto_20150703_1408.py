# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0003_auto_20150701_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.FloatField(null=True, editable=False, blank=True),
        ),
    ]
