# Generated by Django 5.0.2 on 2024-03-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0011_order_is_cancelled_order_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
