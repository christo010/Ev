# Generated by Django 4.2.6 on 2024-03-18 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EvApp', '0003_custuser_is_officer'),
    ]

    operations = [
        migrations.AddField(
            model_name='custuser',
            name='departments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EvApp.department'),
        ),
    ]
