# Generated by Django 4.2.6 on 2024-03-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]