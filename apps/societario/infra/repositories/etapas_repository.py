import uuid
from typing import Optional, List

from apps.societario.infra.models import Etapas


class EtapasRepository:
    def __init__(self, model=Etapas):
        self.__model = model
    
    def get_by_id(self, id: uuid.UUID) -> Optional[Etapas]:
        try:
            return self.__model.objects.get(id=id)
        except self.__model.DoesNotExist:
            return None
    
    def list_etapas(self) -> List[Etapas]:
        return self.__model.objects.all().order_by('ordem')