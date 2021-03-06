# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-29 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0018_auto_20180429_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=255, verbose_name='actor')),
                ('verb', models.CharField(max_length=255, verbose_name='verb')),
                ('message', models.TextField(verbose_name='message')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='date created')),
                ('member_receive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_receive', to='profiles.Membership', verbose_name='member receive')),
                ('member_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_send', to='profiles.Membership', verbose_name='member send')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
