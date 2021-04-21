# Generated by Django 3.2 on 2021-04-21 04:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]