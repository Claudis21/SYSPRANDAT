# Generated by Django 3.2.9 on 2022-05-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_usuario_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='resumen',
            field=models.TextField(blank=True, null=True),
        ),
    ]
