# Generated by Django 4.2.6 on 2024-03-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvApp', '0002_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='custuser',
            name='is_officer',
            field=models.BooleanField(default=False),
        ),
    ]