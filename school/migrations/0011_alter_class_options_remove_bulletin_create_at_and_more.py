# Generated by Django 5.1.7 on 2025-05-14 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_bulletin_bimester_bulletin_create_at_bulletin_year_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'Classes'},
        ),
        migrations.RemoveField(
            model_name='bulletin',
            name='create_at',
        ),
        migrations.AddField(
            model_name='bulletin',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 14, 8, 23, 41, 582743)),
        ),
    ]
