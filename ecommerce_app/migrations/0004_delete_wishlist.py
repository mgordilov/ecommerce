# Generated by Django 5.0.2 on 2024-03-19 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0003_alter_product_business'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WishList',
        ),
    ]