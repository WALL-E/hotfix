# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170818_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patch',
            name='serial_number',
            field=models.IntegerField(default=1),
        ),
    ]
