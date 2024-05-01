# Generated by Django 4.0.3 on 2024-03-10 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0119_remove_customerbalacesheet_billreceive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerbalacesheet',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='core.customer'),
        ),
        migrations.AlterField(
            model_name='customerbalacesheet',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='core.order'),
        ),
        migrations.AlterField(
            model_name='customerbalacesheet',
            name='returnn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='returnn', to='core.returnn'),
        ),
    ]
