# Generated by Django 4.0.3 on 2022-10-22 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_remove_customer_balance_customer_bal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='bal',
        ),
    ]
