# Generated by Django 2.2.dev20180906114925 on 2018-10-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0005_auto_20181013_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro',
            name='golesLocal',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='golesVisitante',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='jornada',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
