# Generated by Django 5.0.3 on 2024-03-12 20:06

import urlapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField()),
                ('name', models.CharField(max_length=200)),
                ('short_url', models.CharField(default=urlapp.models.generate_short_url, max_length=6, unique=True)),
            ],
        ),
    ]
