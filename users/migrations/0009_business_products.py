# Generated by Django 5.0.2 on 2024-03-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0006_order'),
        ('users', '0008_alter_userprofile_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='business_items', to='ecommerce_app.product'),
        ),
    ]