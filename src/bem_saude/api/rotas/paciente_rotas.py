from http import HTTPStatus
from uuid import UUID, uuid7
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from bem_saude.api.schemas.paciente_schemas import PacienteAlterarRequest, PacienteCriarRequest, PacienteResponse
from bem_saude.infraestrutura.banco_dados.conexao import obter_sessao
from bem_saude.infraestrutura.repositorios.repositorio_paciente import RepositorioPaciente
from bem_saude.infraestrutura.banco_dados.modelos.modelo_paciente import ModeloPaciente


router = APIRouter(
    prefix="/pacientes",
    tags=["Paciente"]
)
@router.post(
    "",
    response_model=PacienteResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo paciente",
    responses={
        201:{
            "description": "Paciente criado com sucesso",
            "model": PacienteResponse
        }
    }
)
def criar_paciente(
    dados: PacienteCriarRequest,
    session: Session = Depends(obter_sessao),
) -> PacienteResponse:
    paciente = ModeloPaciente(
        id=uuid7(),
        nome=dados.nome,
        cpf=dados.cpf,
        data_nascimento=dados.data_nasicmento,
        email=dados.email,
        endereco=dados.endereco,
        tipo_sanguineo=dados.tipo_sanguineo,
        observacoes=dados.observacoes
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
def lista_pacientes(
    session: Session = Depends(obter_sessao)):
    repositorio = RepositorioPaciente(sessao=session)
    paciente = repositorio.listar()
    return paciente


@router.get(
    "/{id}",
    response_model=PacienteResponse,
    status_code=status.HTTP_200_OK,
    summary="Buscar paciente filtrando por ID",
    description="""
            Busca um recepcionista específico pelo seu ID (UUID v7).

            Retorna todos os dados do recepcionista, incluindo campos de auditoria.""",
            responses={
                200: {
                    "description": "Paciente encontrado",
                    "model": PacienteResponse
                },
            },
)
def busca_paciente(
    id: UUID,
    session: Session = Depends(obter_sessao)):
    repositorio = RepositorioPaciente(sessao=session)
    paciente = repositorio.buscar_por_id(id)
    if not paciente:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Paciente não encontrado")
    

@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Inativar paciente",
    description="Inativar o paciente quando encontrado.",
    responses={
        204: {
            "description": "Paciente inativado",
        },
    },
)
def inativar_paciente(
     id: UUID, 
    session: Session = Depends(obter_sessao)):
    """Inativa um paciente por ID."""
    repositorio = RepositorioPaciente(sessao=session)
    inativou = repositorio.remover(id)
    if not inativou:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUNT, detail="Paciente não encontrado")


@router.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Alterar dados do paciente",
    responses={
        204: {
            "description": "Paciente alterado"
        },
        404: {
            "description": "Paciente não encontrado"
        }
    }
)
def alterar_paciente(
    id: UUID, 
    dados: PacienteAlterarRequest, 
    session: Session = Depends(obter_sessao)
    ):
    repositorio = RepositorioPaciente(sessao=session)
    inativou = repositorio.editar(id, dados.nome)
    if not inativou:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUNT, detail="Paciente não encontrado")
