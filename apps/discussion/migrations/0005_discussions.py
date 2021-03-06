# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180411_2014'),
        ('discussion', '0004_auto_20180430_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='date created')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account', verbose_name='account')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
