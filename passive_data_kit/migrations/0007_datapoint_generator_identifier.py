# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 20:40
# pylint: skip-file

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0006_auto_20160224_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='generator_identifier',
            field=models.CharField(db_index=True, default='unknown-generator', max_length=1024),
        ),
    ]
