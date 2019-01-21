# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 03:48
# pylint: skip-file

from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models

from ..models import install_supports_jsonfield

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    
    if install_supports_jsonfield():
        operations = [
            migrations.CreateModel(
                name='DataPoint',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('source', models.CharField(max_length=1024)),
                    ('generator', models.CharField(max_length=1024)),
                    ('created', models.DateTimeField()),
                    ('generated_at', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                    ('recorded', models.DateTimeField()),
                    ('properties', django.contrib.postgres.fields.jsonb.JSONField()),
                ],
            ),
        ]
    else:
        operations = [
            migrations.CreateModel(
                name='DataPoint',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('source', models.CharField(max_length=1024)),
                    ('generator', models.CharField(max_length=1024)),
                    ('created', models.DateTimeField()),
                    ('generated_at', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                    ('recorded', models.DateTimeField()),
                    ('properties', models.TextField(max_length=(32 * 1024 * 1024 * 1024))),
                ],
            ),
        ]