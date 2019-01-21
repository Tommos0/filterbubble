# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-12 02:43
# pylint: skip-file

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0013_datafile'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='data_bundle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_files', to='passive_data_kit.DataBundle'),
        ),
        migrations.AlterField(
            model_name='datafile',
            name='data_point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_files', to='passive_data_kit.DataPoint'),
        ),
    ]