# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-01 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0005_remove_invoice_particulars'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceparticulars',
            name='particulars',
            field=models.TextField(blank=True, null=True),
        ),
    ]
