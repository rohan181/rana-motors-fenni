# Generated by Django 4.0.3 on 2023-09-06 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0104_remove_mrentryrecord_order_mrentryrecord_mrentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoicenumber',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
