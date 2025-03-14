# Generated by Django 5.1.1 on 2024-12-19 16:38

import django.contrib.postgres.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidades', '0003_rename_abertura_contabilidade_data_abertura'),
        ('societario', '0010_rename_staustarefa_statustarefa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rua', models.CharField(max_length=80)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=80)),
                ('complemento', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('municipio', models.CharField(max_length=80)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='InfoAdicionais',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('resp_tecnica', models.BooleanField(default=False)),
                ('nome_reponsavel', models.CharField(blank=True, max_length=80, null=True)),
                ('nmr_carteira_profissional', models.CharField(blank=True, max_length=11, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
                ('area_resp', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='processo',
            name='contabilidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processos', to='contabilidades.contabilidade'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='tipo_processo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processos', to='societario.tipoprocesso'),
        ),
        migrations.CreateModel(
            name='FormularioAbertura',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('opcoes_nome_empresa', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120), size=None)),
                ('nome_fantasia', models.CharField(max_length=120)),
                ('inscricao_imob', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('val_capital_social', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capital_integralizado', models.BooleanField(default=True)),
                ('data_integralizacao', models.DateField(blank=True, null=True)),
                ('empresa_anexa_resid', models.BooleanField(default=False)),
                ('endereco_apenas_contato', models.BooleanField(default=False)),
                ('area_empresa', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='societario.endereco')),
                ('processo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='formulario', to='societario.processo')),
                ('info_adic', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societario.infoadicionais')),
            ],
        ),
    ]
