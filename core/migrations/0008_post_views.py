# Generated by Django 3.2 on 2021-04-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_banner_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
