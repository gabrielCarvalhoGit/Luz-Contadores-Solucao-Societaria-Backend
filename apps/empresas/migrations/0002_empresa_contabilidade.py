# Generated by Django 5.1.1 on 2024-09-25 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidades', '0002_alter_contabilidade_nome_fantasia'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='contabilidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contabilidades.contabilidade'),
        ),
    ]