"""
Schemas Pydantic para Pacientes.

Define os DTOs (Data Transfer Objects) para requisições e respostas relacionadas
a pacientes.
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from bem_saude.dominio.enums.status_cadastro import StatusCadastro


class PacienteCriarRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nome completo do paciente.",
        examples=["Ana Paula Ferreira"]
    )

    status: str = Field(
        default=StatusCadastro.ATIVO,
        description="Status do cadastro do paciente.",
        examples=["ATIVO"]
    )

    cpf: str = Field(
        ...,
        max_length=14,
        description="CPF do paciente",
        examples=["123.456.789-10"]
    )

    data_nascimento: datetime = Field(
        ...,
        description="Data de nascimento do paciente",
        examples=["1997-12-03"]
    )

    telefone: str = Field(
        ...,
        max_length=15,
        description="Telefone do paciente.",
        examples=["(47)91234-4321"]
    )

    email: str = Field(
        ...,
        max_length=60,
        description="E-mail cadastrado do paciente",
        examples=["anaferreira@hotmail.com"]
    )

    endereco: str = Field(
        ...,
        max_length=45,
        description="Endereço cadastrado do paciente.",
        examples=["Rua dos Caçadores, 191"]
    )

    tipo_sanguineo: str = Field(
        ...,
        description="Tipo Sanguíneo do paciente.",
        examples=["O+"]
    )

    observacoes: str = Field(
        ...,
        description="Observações do paciente.",
        examples=[""]
    )

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                "nome": "Ana Paula Ferreira",
                "status": "ATIVO",
                "cpf": "123.456.789-10",
                "data_nascimento": "1997-12-03",
                "telefone": "(47)91234-4321",
                "email": "anaferreira@hotmail.com",
                "endereco": "Rua dos Caçadores, 191",
                "tipo_sanguineo": "O+",
                "observacoes": "",
            }
            ]
        }
    }


class PacienteAlterarRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nome completo do paciente.",
        examples=["Ana Paula Ferreira"]
    )

    telefone: str = Field(
        ...,
        max_length=15,
        description="Telefone do paciente.",
        examples=["(47)91234-4321"]
    )

    email: str = Field(
        ...,
        max_length=60,
        description="E-mail cadastrado do paciente",
        examples=["anaferreira@hotmail.com"]
    )

    endereco: str = Field(
        ...,
        max_length=45,
        description="Endereço cadastrado do paciente.",
        examples=["Rua dos Caçadores, 191"]
    )

    observacoes: str = Field(
        ...,
        description="Observações do paciente.",
        examples=[""]
    )

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                "nome": "Ana Paula Ferreira",
                "telefone": "(47)91234-4321",
                "email": "anaferreira@hotmail.com",
                "endereco": "Rua dos Caçadores, 191",
                "observacoes": "",
            }
            ]
        }
    }


class PacienteResponse(BaseModel):
    id : UUID = Field(
        ...,
        description="Identificador (UUID v7) único do paciente.",
        examples=["019c4cba-31a4-7db7-9097-de70dcaf012b"]
    )

    nome: str = Field(
        ...,
        description="Nome completo do paciente.",
        examples=["Ana Paula Ferreira"]
    )

    status: str = Field(
        ...,
        description="Status do cadastro do paciente.",
        examples=["ATIVO"]
    )

    cpf: str = Field(
        ...,
        description="CPF do paciente",
        examples=["123.456.789-10"]
    )

    data_nascimento: datetime = Field(
        ...,
        description="Data de nascimento do paciente",
        examples=["1997-12-03"]
    )

    telefone: str = Field(
        ...,
        description="Telefone do paciente.",
        examples=["(47)91234-4321"]
    )

    email: str = Field(
        ...,
        description="E-mail cadastrado do paciente",
        examples=["anaferreira@hotmail.com"]
    )

    endereco: str = Field(
        ...,
        description="Endereço cadastrado do paciente.",
        examples=["Rua dos Caçadores, 191"]
    )

    tipo_sanguineo: str = Field(
        ...,
        description="Tipo Sanguíneo do paciente.",
        examples=["O+"]
    )

    observacoes: str = Field(
        ...,
        description="Observações do paciente.",
        examples=[""]
    )

    criado_em: datetime = Field(
        ...,
        description="Data e hora de criação do registro.",
        examples=["2026-02-11T10:30:00"]
    )

    alterado_em: datetime | None = Field(
        None,
        description="Data e hora da última alteração do registro.",
        examples=["2026-02-12T11:45:00"]
    )

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                "nome": "Ana Paula Ferreira",
                "status": "ATIVO",
                "cpf": "123.456.789-10",
                "data_nascimento": "1997-12-03",
                "telefone": "(47)91234-4321",
                "email": "anaferreira@hotmail.com",
                "endereco": "Rua dos Caçadores, 191",
                "tipo_sanguineo": "O+",
                "observacoes": "",
                "criado_em": "2026-02-11T10:30:00",
                "alterado_em": None
            }
            ]
        }
    }
