# Generated by Django 2.2.dev20180906114925 on 2018-10-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0002_auto_20181013_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuentro',
            name='jornada',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
