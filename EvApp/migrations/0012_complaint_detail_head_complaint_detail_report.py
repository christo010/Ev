# Generated by Django 4.2.6 on 2024-03-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvApp', '0011_complaint_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='detail_head',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='detail_report',
            field=models.TextField(null=True),
        ),
    ]
