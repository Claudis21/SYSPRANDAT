# Generated by Django 3.2.9 on 2022-05-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_documento_palabras_clave'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='archivos/'),
        ),
    ]
