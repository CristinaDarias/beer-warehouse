# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-01 12:57
from __future__ import unicode_literals

import random

from django.db import migrations, models


def gen_tax_number(apps, schema_editor):
    MyModel = apps.get_model('beers', 'Company')
    for row in MyModel.objects.all():
        row.tax_number = random.randint(1, 1000)
        row.save(update_fields=['tax_number'])


class Migration(migrations.Migration):
    dependencies = [
        ('beers', '0004_auto_20200701_1357'),
    ]

    operations = [
        migrations.RunPython(gen_tax_number, reverse_code=migrations.RunPython.noop),
    ]
