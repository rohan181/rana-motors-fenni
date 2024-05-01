# Generated by Django 4.0.3 on 2022-07-01 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_sold_customerupdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sold',
            name='solddt',
        ),
        migrations.AddField(
            model_name='sold',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sold',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
    ]
