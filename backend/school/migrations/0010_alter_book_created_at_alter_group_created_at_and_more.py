# Generated by Django 5.1.7 on 2025-06-14 17:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_alter_book_created_at_alter_book_tenant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 14, 14, 42, 54, 702317), editable=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 14, 14, 42, 54, 700090), editable=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='itinerary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to='school.itinerary', verbose_name='Itinerário da turma'),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 14, 14, 42, 54, 699497), editable=False),
        ),
        migrations.AlterField(
            model_name='professor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 14, 14, 42, 54, 700911), editable=False),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 14, 14, 42, 54, 702994), editable=False),
        ),
        migrations.AlterField(
            model_name='schoolrecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 14, 14, 42, 54, 701664), editable=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 14, 14, 42, 54, 698908), editable=False),
        ),
    ]
