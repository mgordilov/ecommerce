# Generated by Django 5.0.2 on 2024-03-27 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_userprofile_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='customer_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
