# Generated by Django 3.2.9 on 2022-05-22 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20220520_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
    ]