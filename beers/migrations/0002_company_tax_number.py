# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-01 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='tax_number',
            field=models.IntegerField(default=9, verbose_name='Tax number'),
            preserve_default=False,
        ),
    ]
