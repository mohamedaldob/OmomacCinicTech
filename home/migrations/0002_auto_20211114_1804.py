# Generated by Django 3.2.9 on 2021-11-14 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_visiting',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='visiting',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
