# Generated by Django 5.0.2 on 2024-03-25 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_business_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='products',
        ),
    ]
