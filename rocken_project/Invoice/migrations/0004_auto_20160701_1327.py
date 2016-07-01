# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-01 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0003_auto_20160701_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('invoiceName', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('clientContactPersonName', models.CharField(blank=True, max_length=100, null=True)),
                ('clientContactPersonEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('clientContactPersonNo', models.IntegerField(blank=True, null=True)),
                ('termsAndConditions', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Invoice.CompanyCreation')),
            ],
        ),
        migrations.RemoveField(
            model_name='registerclient',
            name='company',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='clientAddress',
            new_name='clientAddresscopy',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='companyName',
            new_name='client_invoice_name_copy',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='contactPerson',
            new_name='contactPersonNamecopy',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='contactPersonNo',
            new_name='contactPersonNocopy',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='footer',
            new_name='termsAndConditionscopy',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='clientName',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='serviceTaxAmount',
        ),
        migrations.RemoveField(
            model_name='invoiceparticulars',
            name='particulars',
        ),
        migrations.RemoveField(
            model_name='invoiceparticulars',
            name='period',
        ),
        migrations.AddField(
            model_name='invoiceparticulars',
            name='invoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Invoice.Invoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceparticulars',
            name='periodInDays',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='particulars',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='RegisterClient',
        ),
        migrations.AddField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Invoice.Client'),
        ),
    ]
