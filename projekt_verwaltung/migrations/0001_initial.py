# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('fn', models.CharField(max_length=30)),
                ('ln', models.CharField(max_length=30)),
                ('firm', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('telefon', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('client', models.ForeignKey(to='projekt_verwaltung.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('fn', models.CharField(max_length=30)),
                ('ln', models.CharField(max_length=30)),
                ('mother_language', models.CharField(max_length=30)),
                ('trans_language', models.CharField(max_length=30)),
                ('telefon', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='translator',
            field=models.ManyToManyField(to='projekt_verwaltung.Translator'),
        ),
    ]
