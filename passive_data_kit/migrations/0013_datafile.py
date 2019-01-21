# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-12 02:25
# pylint: skip-file

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0012_auto_20160319_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(db_index=True, max_length=256)),
                ('content_file', models.FileField(upload_to='data_files')),
                ('data_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_files', to='passive_data_kit.DataPoint')),
            ],
        ),
    ]
