# Generated by Django 5.1.1 on 2024-10-19 02:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0005_processos'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtapaProcesso',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societario.etapas')),
                ('nome_processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societario.nomeprocessos')),
            ],
        ),
    ]