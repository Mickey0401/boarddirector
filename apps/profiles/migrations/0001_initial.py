# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 09:19
from __future__ import unicode_literals

import common.utils
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('committees', '0001_initial'),
        ('accounts', '0002_account_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined_board', models.DateField(default=django.utils.timezone.now, verbose_name='date joined board')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name='phone number')),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'Administrator'), (1, 'Board Chair'), (20, 'CEO'), (21, 'Executive Director'), (2, 'Board Member'), (3, 'Executive Assistant'), (4, 'Guest'), (5, 'Vendor'), (6, 'Staff'), (7, 'Consultant')], default=0, verbose_name='role')),
                ('is_active', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=True, verbose_name='active')),
                ('term_start', models.DateField(blank=True, null=True, verbose_name='starts')),
                ('term_expires', models.DateField(blank=True, null=True, verbose_name='expires')),
                ('timezone', timezone_field.fields.TimeZoneField(default=b'America/Chicago')),
                ('employer', models.CharField(blank=True, max_length=255, verbose_name='employer')),
                ('job_title', models.CharField(blank=True, max_length=255, verbose_name='job title')),
                ('work_email', models.CharField(blank=True, max_length=255, verbose_name='work email')),
                ('work_number', models.CharField(blank=True, max_length=255, verbose_name='work number')),
                ('intro', models.CharField(blank=True, max_length=250, verbose_name='intro')),
                ('bio', models.TextField(blank=True, verbose_name='bio')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='address')),
                ('secondary_address', models.CharField(blank=True, max_length=255, verbose_name='secondary address')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='city')),
                ('state', models.CharField(blank=True, max_length=50, verbose_name='state')),
                ('zip', models.CharField(blank=True, max_length=50, verbose_name='zip')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='country')),
                ('birth_date', models.CharField(blank=True, max_length=100, verbose_name='birth date')),
                ('secondary_phone', models.CharField(blank=True, max_length=255, verbose_name='secondary phone')),
                ('affiliation', models.CharField(blank=True, max_length=255, verbose_name='affiliations')),
                ('social_media_link', models.CharField(blank=True, max_length=255, verbose_name='social media links')),
                ('avatar', models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/avatars/', location=b'/vagrant/public/media/avatars'), upload_to=common.utils.avatar_upload_to)),
                ('position', models.CharField(blank=True, max_length=250, verbose_name='position')),
                ('last_login', models.DateTimeField(editable=False, null=True, verbose_name='last login')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified date')),
                ('invitation_status', models.PositiveSmallIntegerField(choices=[(0, b'NOT_SENT'), (1, b'SENT'), (2, b'INVITED')], default=0, verbose_name='invitation status')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='accounts.Account')),
                ('assistant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bosses', to='profiles.Membership')),
                ('committees', models.ManyToManyField(blank=True, null=True, related_name='memberships', to='committees.Committee', verbose_name='committees')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('first_name', 'last_name'),
            },
        ),
        migrations.CreateModel(
            name='TemporaryUserPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tmppswd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='accounts',
            field=models.ManyToManyField(null=True, related_name='users', through='profiles.Membership', to='accounts.Account', verbose_name='accounts'),
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('user', 'account')]),
        ),
    ]
