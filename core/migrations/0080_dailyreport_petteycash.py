# Generated by Django 4.0.3 on 2022-11-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0079_dailyreport_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreport',
            name='petteyCash',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
