# Generated by Django 5.0.2 on 2024-03-25 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0007_remove_order_product_order_product'),
        ('users', '0011_userprofile_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='order',
            field=models.ManyToManyField(blank=True, related_name='orders', to='ecommerce_app.order'),
        ),
    ]
