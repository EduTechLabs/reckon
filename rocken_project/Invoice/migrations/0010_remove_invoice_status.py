# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-07 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0009_auto_20160706_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='status',
        ),
    ]