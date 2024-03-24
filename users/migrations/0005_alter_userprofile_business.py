# Generated by Django 5.0.2 on 2024-03-19 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.business'),
        ),
    ]