# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrooge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract',
            field=models.CharField(blank=True, max_length=320),
        ),
    ]
