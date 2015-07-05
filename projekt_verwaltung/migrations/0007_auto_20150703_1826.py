# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0006_auto_20150703_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
