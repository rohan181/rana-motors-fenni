# Generated by Django 4.0.3 on 2024-06-20 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0167_alter_product_groupname_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='temppaybill',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='reporttype',
            field=models.CharField(blank=True, choices=[('COMMISION', 'COMMISION'), ('DISCOUNT', 'DISCOUNT'), ('FUND TRANSFER', 'FUND TRANSFER'), ('CORPORATE', 'CORPORATE')], max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('local', 'local'), ('public', 'public')], default='public', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='temppaybill',
            name='ammount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
