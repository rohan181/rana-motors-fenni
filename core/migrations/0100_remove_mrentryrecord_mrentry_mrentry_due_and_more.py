# Generated by Django 4.0.3 on 2023-08-28 05:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0099_corportepay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mrentryrecord',
            name='mrentry',
        ),
        migrations.AddField(
            model_name='mrentry',
            name='due',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='mrentry',
            name='totalprice',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='mrentry',
            name='totalprice1',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='mrentry',
            name='vehicleno',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='Phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='costprice',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='engine_no',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='exchange_ammount',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.order'),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='price2',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='sparename',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useritem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='core.product'),
        ),
    ]
