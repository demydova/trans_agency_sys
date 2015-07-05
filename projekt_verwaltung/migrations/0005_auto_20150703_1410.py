# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0004_auto_20150703_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.FloatField(null=True, editable=False),
        ),
    ]
