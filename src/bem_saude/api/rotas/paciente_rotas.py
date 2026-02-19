from http import HTTPStatus
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid6 import uuid7

from bem_saude.api.auth import validar_token
from bem_saude.infraestrutura.banco_dados.conexao import obter_sessao
from bem_saude.infraestrutura.banco_dados.modelos.modelo_paciente import ModeloPaciente
from bem_saude.infraestrutura.repositorios.repositorio_paciente import RepositorioPaciente
from bem_saude.api.schemas.pacientes_schemas import PacienteAlterarRequest, PacienteCriarRequest, PacienteResponse


router = APIRouter(
    prefix="/pacientes",
    tags=["Paciente"],
    dependencies=[Depends(validar_token)]
)
@router.post(
    "",
    response_model=PacienteResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo paciente",
    responses={
        201: {
            "description": "Paciente criado com sucesso.",
            "model": PacienteResponse
        },
    },
)
def criar_paciente(
    dados: PacienteCriarRequest,
    session: Session = Depends(obter_sessao)
) -> PacienteResponse:
    """Cadastrar um paciente."""
    paciente = ModeloPaciente(
        id=uuid7(),
        nome=dados.nome,
        status=dados.status,
        cpf=dados.cpf,
        email=dados.email,
        telefone=dados.telefone,
        tipo_sanguineo=dados.tipo_sanguineo,
        observacoes=dados.observacoes,
        endereco=dados.endereco,
        data_nascimento=dados.data_nascimento,
    )
    repositorio = RepositorioPaciente(sessao=session)
    paciente = repositorio.criar(paciente)
    return paciente


@router.get(
    "",
    response_model=list[PacienteResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar pacientes",
    responses={
        200: {
            "description": "Lista de pacientes",
            "model": list[PacienteResponse]
        },
    },
)
def listar_pacientes(session: Session = Depends(obter_sessao)):
    """Listagem de todos os pacientes cadastrados."""
    repositorio = RepositorioPaciente(sessao=session)
    pacientes = repositorio.listar()
    return pacientes


@router.get(
    "/{id}",
    response_model=PacienteResponse,
    status_code=status.HTTP_200_OK,
    summary="Buscar paciente filtrando por ID",
    description="""
            Busca um paciente específico pelo seu ID (UUID v7).""",
    responses={
        200: {
            "description": "Paciente encontrado",
            "model": PacienteResponse
        },
    },
)
def buscar_paciente(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Busca um paciente por seu ID."""
    repositorio = RepositorioPaciente(sessao=session)
    paciente = repositorio.buscar_por_id(id)
    if not paciente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Paciente não encontrado."
            )
    
    return paciente


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Inativar um paciente.",
    description="Inativar o paciente quando encontrado.",
    responses={
        204: {
            "description": "Paciente encontrado e inativado."
        },
    },
)
def inativar_paciente(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    """Inativa um paciente por seu ID."""

    repositorio = RepositorioPaciente(sessao=session)
    inativou = repositorio.inativar(id)
    if not inativou:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Paciente não encontrado."
            )
    

@router.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Alterar os dados de um paciente.",
    responses={
        204: {
            "description": "Paciente encontrado e modificado."
        },
        404: {
            "description": "Paciente não encontrado."
        },
    },
)
def alterar_paciente(
    id: UUID,
    dados: PacienteAlterarRequest,
    session: Session = Depends(obter_sessao)
):
    """Alterar os dados de um paciente por seu ID."""
    repositorio = RepositorioPaciente(sessao=session)
    alterou = repositorio.editar(
        id,
        dados.nome,
        dados.email,
        dados.endereco,
        dados.telefone,
        dados.observacoes
    )
    if not alterou:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail="Paciente não encontrado."
            )
    

@router.put(
    "/{id}/ativar",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Ativar paciente",
    responses={
        204: {
            "description": "Paciente ativado com sucesso"
        },
        404: {
            "description": "Paciente não encontrado"
        },
    },
)
def ativar_paciente(
    id: UUID,
    session: Session = Depends(obter_sessao)
):
    repositorio = RepositorioPaciente(sessao=session)
    ativou = repositorio.ativar(id)
    if not ativou:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Paciente não encontrado")
