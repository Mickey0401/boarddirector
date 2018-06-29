# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0008_meeting_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='committee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meetings', to='committees.Committee', verbose_name='committee'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to='profiles.Membership'),
        ),
    ]
