# Generated by Django 3.2.9 on 2021-11-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211114_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_visiting',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
