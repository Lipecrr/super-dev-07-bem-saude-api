"""
Schemas Pydantic para Profissional.

Define os DTOs (Data Transfer Objects) para requisições e respostas relacionadas
a profissionais.
"""

from uuid import UUID
from pydantic import BaseModel, Field


class ProfissionalCriarRequest(BaseModel):
    """
    Schema para criação de profissional.

    Validações:
    - nome: mínimo 3 caracteres, máximo 255 caracteres
    - especialidade: máximo 50 caracteres
    - registro: máximo 20 caracteres
    - duracao: máximo 10 caracteres
    """
    nome: str = Field(
        ...,
        min_length=3,
        max_length=255,
        description="Nome completo do profissional",
        examples=["Dr. João Silva"]
    )
    especialidade: str = Field(
        ...,
        max_length=50,
        description="Especialidade médica",
        examples=["Cardiologia"]
    )
    registro: str = Field(
        ...,
        max_length=20,
        description="Registro profissional (CRM)",
        examples=["CRM 12345"]
    )
    duracao: str = Field(
        ...,
        max_length=10,
        description="Duração da consulta em minutos",
        examples=["30"]
    )
    valor: str = Field(
        "",
        max_length=15,
        description="Valor da consulta",
        examples=["150,00"]
    )
    dias_semana: str = Field(
        "",
        max_length=100,
        description="Dias da semana de atendimento separados por vírgula",
        examples=["SEG,TER,QUA,QUI,SEX"]
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Dr. João Silva",
                    "especialidade": "Cardiologia",
                    "registro": "CRM 12345",
                    "duracao": "30",
                    "valor": "150,00",
                    "dias_semana": "SEG,TER,QUA,QUI,SEX"
                }
            ]
        }
    }


class ProfissionalEditarRequest(BaseModel):
    """
    Schema para alteração de profissional.

    Validações:
    - nome: mínimo 3 caracteres, máximo 255 caracteres
    - especialidade: máximo 50 caracteres
    - duracao: máximo 10 caracteres
    """
    nome: str = Field(
        ...,
        min_length=3,
        max_length=255,
        description="Nome completo do profissional",
        examples=["Dr. João Silva"]
    )
    especialidade: str = Field(
        ...,
        max_length=50,
        description="Especialidade médica",
        examples=["Cardiologia"]
    )
    duracao: str = Field(
        ...,
        max_length=10,
        description="Duração da consulta em minutos",
        examples=["30"]
    )
    valor: str = Field(
        "",
        max_length=15,
        description="Valor da consulta",
        examples=["150,00"]
    )
    dias_semana: str = Field(
        "",
        max_length=100,
        description="Dias da semana de atendimento separados por vírgula",
        examples=["SEG,TER,QUA,QUI,SEX"]
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Dr. João Silva",
                    "especialidade": "Cardiologia",
                    "duracao": "30",
                    "valor": "150,00",
                    "dias_semana": "SEG,TER,QUA,QUI,SEX"
                }
            ]
        }
    }


class ProfissionalResponse(BaseModel):
    """
    Schema de resposta de profissional para listagem.

    Retorna dados resumidos do profissional.
    Status é retornado como boolean (True = ATIVO, False = INATIVO).
    """
    id: UUID = Field(
        ...,
        description="Identificador único do profissional (UUID v7)",
        examples=["019c445a-ae15-7bcd-ba0a-cd7b0d0e3f26"]
    )
    nome: str = Field(
        ...,
        description="Nome completo do profissional",
        examples=["Dr. João Silva"]
    )
    duracao: str = Field(
        ...,
        description="Duração da consulta em minutos",
        examples=["30"]
    )
    especialidade: str = Field(
        ...,
        description="Especialidade médica",
        examples=["Cardiologia"]
    )
    registro: str = Field(
        ...,
        description="Registro profissional (CRM)",
        examples=["CRM 12345"]
    )
    status: bool = Field(
        ...,
        description="Status do cadastro (true = ativo, false = inativo)",
        examples=[True]
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": "019c445a-ae15-7bcd-ba0a-cd7b0d0e3f26",
                    "nome": "Dr. João Silva",
                    "duracao": "30",
                    "especialidade": "Cardiologia",
                    "registro": "CRM 12345",
                    "status": True
                }
            ]
        }
    }


class ProfissionalPesquisaResponse(BaseModel):
    """
    Schema de resposta detalhada de profissional (busca por ID).

    Retorna todos os dados do profissional.
    Status é retornado como boolean (True = ATIVO, False = INATIVO).
    """
    id: UUID = Field(
        ...,
        description="Identificador único do profissional (UUID v7)",
        examples=["019c445a-ae15-7bcd-ba0a-cd7b0d0e3f26"]
    )
    nome: str = Field(
        ...,
        description="Nome completo do profissional",
        examples=["Dr. João Silva"]
    )
    especialidade: str = Field(
        ...,
        description="Especialidade médica",
        examples=["Cardiologia"]
    )
    registro: str = Field(
        ...,
        description="Registro profissional (CRM)",
        examples=["CRM 12345"]
    )
    duracao: str = Field(
        ...,
        description="Duração da consulta em minutos",
        examples=["30"]
    )
    valor: str | None = Field(
        None,
        description="Valor da consulta",
        examples=["150,00"]
    )
    dias_semana: str | None = Field(
        None,
        description="Dias da semana de atendimento",
        examples=["SEG,TER,QUA,QUI,SEX"]
    )
    status: bool = Field(
        ...,
        description="Status do cadastro (true = ativo, false = inativo)",
        examples=[True]
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": "019c445a-ae15-7bcd-ba0a-cd7b0d0e3f26",
                    "nome": "Dr. João Silva",
                    "especialidade": "Cardiologia",
                    "registro": "CRM 12345",
                    "duracao": "30",
                    "valor": "150,00",
                    "dias_semana": "SEG,TER,QUA,QUI,SEX",
                    "status": True
                }
            ]
        }
    }
