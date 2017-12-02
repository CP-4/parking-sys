# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShawPark',
            fields=[
                ('parkid', models.IntegerField(primary_key=True, serialize=False)),
                ('logi', models.IntegerField(default=0)),
                ('leti', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
