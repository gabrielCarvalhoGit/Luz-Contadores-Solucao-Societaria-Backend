# Generated by Django 5.1.1 on 2024-10-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0004_alter_aberturaempresa_expire_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='nome_etapa',
            field=models.CharField(max_length=20),
        ),
    ]
