# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paulApp', '0002_delete_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('load_no', models.IntegerField(unique=True)),
                ('model_no', models.IntegerField()),
                ('vehicle_name', models.CharField(max_length=100)),
            ],
        ),
    ]
