# Generated by Django 5.0.4 on 2024-04-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_porpertybook_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
