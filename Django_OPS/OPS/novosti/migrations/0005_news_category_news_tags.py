# Generated by Django 5.1.2 on 2024-11-06 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novosti', '0004_category_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novosti.category'),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, to='novosti.tag'),
        ),
    ]