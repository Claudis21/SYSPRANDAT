# Generated by Django 3.2.9 on 2022-05-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_usuario_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
