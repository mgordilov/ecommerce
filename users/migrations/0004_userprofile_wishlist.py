# Generated by Django 5.0.2 on 2024-03-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0003_alter_product_business'),
        ('users', '0003_remove_userprofile_stripe_id_business_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wishlist',
            field=models.ManyToManyField(blank=True, null=True, to='ecommerce_app.product'),
        ),
    ]
