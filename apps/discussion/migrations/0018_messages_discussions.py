# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0017_auto_20180530_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='discussions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='discussion.Discussions', verbose_name='Discussions id'),
        ),
    ]
