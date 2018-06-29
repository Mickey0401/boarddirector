# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0013_auto_20180203_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='audittrail',
            name='size',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='file size'),
        ),
        migrations.AddField(
            model_name='document',
            name='size',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='file size'),
        ),
    ]