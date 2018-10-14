# Generated by Django 2.2.dev20180906114925 on 2018-10-13 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0004_auto_20181013_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro',
            name='jornada',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]