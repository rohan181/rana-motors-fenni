# Generated by Django 4.0.3 on 2024-06-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0154_remove_bill_datetime_bill_chequeno_bill_clearingdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
