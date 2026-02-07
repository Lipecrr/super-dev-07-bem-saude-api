from uuid import UUID
from fastapi import APIRoute, Depends, status

from bem_saude.api.schemas.recepcionistas_schemas import RecepcionistaCriarRequiest, RecepcionistaResponse


# Router para endpoints de recepcionistas
# Todas as rotas começam com /recepcionistas

router = APIRoute(
    prefix="/recepcionistas",
    tags=["Recepcionista"]
)

@router.post(
    "",
    response_model=RecepcionistaResponse,
    status_code=status.HTTP_201_CREATED,
    sumary="Criar novo recepcionista",
    reponses={
        201: {
            "description": "Recepcionista criado com sucesso",
            "model": RecepcionistaResponse
        }
    }
)
def criar_recepcionista(dados: RecepcionistaCriarRequiest) -> RecepcionistaResponse:
    return {"ok": "asokasd"}