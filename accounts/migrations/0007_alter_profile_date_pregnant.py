# Generated by Django 3.2.9 on 2021-11-14 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_date_pregnant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_pregnant',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
