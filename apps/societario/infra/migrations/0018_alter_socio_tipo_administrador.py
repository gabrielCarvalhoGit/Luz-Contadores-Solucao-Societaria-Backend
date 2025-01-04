# Generated by Django 5.1.1 on 2025-01-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0017_alter_socio_orgao_expedidor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='tipo_administrador',
            field=models.CharField(blank=True, choices=[('conjunto', 'Conjunto'), ('isoladamente', 'Isoladamente'), ('nao_aplica', 'Não se aplica')], max_length=15, null=True),
        ),
    ]
