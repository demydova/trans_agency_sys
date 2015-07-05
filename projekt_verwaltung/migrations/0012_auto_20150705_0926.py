# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_verwaltung', '0011_auto_20150705_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='word_rate',
            new_name='page_rate',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='words_number',
            new_name='pages_number',
        ),
    ]
