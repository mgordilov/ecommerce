# Generated by Django 5.0.2 on 2024-03-28 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0010_product_shortened_description_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
