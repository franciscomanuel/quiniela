# Generated by Django 2.2.dev20180906114925 on 2018-10-13 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0006_auto_20181013_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuentro',
            name='liga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estadisticas.Liga'),
        ),
    ]
