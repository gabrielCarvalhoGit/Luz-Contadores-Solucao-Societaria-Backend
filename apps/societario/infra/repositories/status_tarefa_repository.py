import uuid
from typing import List

from apps.societario.infra.models import StatusTarefa
from apps.societario.domain.entities.status_tarefa import StatusTarefaEntity


class StatusTarefaRepository:
    def __init__(self, model=StatusTarefa):
        self.__model = model

    def bulk_create(self, data: List[StatusTarefaEntity]) -> List[StatusTarefa]:
        status_tarefa_models = [
            StatusTarefa(
                processo_id=item.processo.id,
                etapa_id=item.etapa.id,
                tarefa_id=item.tarefa.id,
                concluida=item.concluida,
                sequencia=item.sequencia
            ) for item in data
        ]
        return StatusTarefa.objects.bulk_create(status_tarefa_models)
    
    def filter_status_tarefas(self, processo_id: uuid.UUID) -> List[StatusTarefa]:
        return StatusTarefa.objects.filter(processo_id=processo_id).select_related(
            'tarefa', 
            'etapa'
        ).order_by('sequencia')