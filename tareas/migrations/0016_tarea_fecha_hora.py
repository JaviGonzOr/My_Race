# Generated by Django 4.1.3 on 2025-04-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0015_rename_interlagos_resultadocarrera_alemania_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_hora',
            field=models.TextField(blank=True, null=True),
        ),
    ]
