# Generated by Django 5.1.1 on 2024-12-04 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0004_tarefa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='etapa_inicial',
        ),
    ]
