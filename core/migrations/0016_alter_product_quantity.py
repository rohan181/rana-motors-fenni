# Generated by Django 4.0.3 on 2022-06-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_product_brand_product_productcatagory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
