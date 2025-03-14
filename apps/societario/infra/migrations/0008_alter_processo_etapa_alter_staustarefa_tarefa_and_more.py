# Generated by Django 5.1.1 on 2024-12-04 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0007_alter_processo_etapa_alter_tarefa_etapa_staustarefa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='etapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processos', to='societario.etapa'),
        ),
        migrations.AlterField(
            model_name='staustarefa',
            name='tarefa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_tarefas', to='societario.tarefa'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='etapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tarefas', to='societario.etapa'),
        ),
    ]
