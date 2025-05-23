# Generated by Django 5.1.7 on 2025-05-14 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_book_author_book_name_alter_bulletin_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='presence',
            field=models.JSONField(null=True, verbose_name='JSON Values of Grades'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 14, 9, 12, 33, 591227)),
        ),
    ]
