# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-01 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name=b'Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name=b'Last modified at')),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bars_bar_created', to=settings.AUTH_USER_MODEL, verbose_name=b'Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bars_bar_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name=b'Last modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
