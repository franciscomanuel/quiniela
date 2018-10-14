# Generated by Django 2.2.dev20180906114925 on 2018-10-13 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='liga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estadisticas.Liga'),
        ),
    ]