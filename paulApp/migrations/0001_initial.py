# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DriverModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('dl_no', models.CharField(unique=True, max_length=100)),
                ('dl_expiry', models.DateField()),
                ('finished_tasks', models.IntegerField(default=0)),
                ('assigned_tasks', models.IntegerField(default=0)),
                ('reputation', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('load', models.IntegerField()),
                ('status', models.CharField(default=b'Pending', max_length=50, choices=[(b'Dispatched', b'Dispatched'), (b'Pending', b'Pending'), (b'Complete', b'Complete'), (b'Loaded', b'Loaded'), (b'Unloaded', b'Unloaded')])),
                ('customer', models.CharField(max_length=200)),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('usd', models.IntegerField()),
                ('ship_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('del_date', models.DateTimeField(default=b'')),
                ('vehicle_type', models.CharField(max_length=100)),
                ('total_km', models.IntegerField()),
                ('equipment_type', models.CharField(max_length=200)),
                ('driver_name', models.ForeignKey(related_name='driver', to='paulApp.DriverModel', to_field=b'dl_no')),
            ],
        ),
    ]
