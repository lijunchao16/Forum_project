# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 12:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u6807\u9898')),
                ('des', models.CharField(max_length=150, verbose_name='\u63cf\u8ff0')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005')),
            ],
            options={
                'verbose_name': '\u677f\u5757',
                'verbose_name_plural': '\u677f\u5757',
            },
        ),
    ]
