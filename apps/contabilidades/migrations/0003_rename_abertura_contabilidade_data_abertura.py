# Generated by Django 5.1.1 on 2024-10-01 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidades', '0002_alter_contabilidade_nome_fantasia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contabilidade',
            old_name='abertura',
            new_name='data_abertura',
        ),
    ]
