# Generated by Django 5.0.2 on 2024-03-06 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='type',
            field=models.CharField(choices=[('individual', 'Individual'), ('company', 'Company'), ('non_profit', 'Non-Profit')], default='individual', max_length=200),
        ),
    ]
