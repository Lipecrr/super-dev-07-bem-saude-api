from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from bem_saude.dominio.enums.status_cadastro import StatusCadastro


class PacienteCriarRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nome completo do paciente",
        example="Felipe Fernando Corrêa"
    )
    telefone: str = Field(
        ...,
        max_length=15,
        description="Telefone do paciente",
        example="(99) 99999-9999"
    )
    cpf: str = Field(
        ...,
        max_length=14,
        description="CPF do paciente",
        example="999.999.999-99"
    )
    data_nascimento: datetime = Field(
        ...,
        description="Data de nascimento do paciente",
        example="1999-02-13"
    )
    email: str = Field(
        ...,
        max_length=60,
        description="Email do paciente",
        example="felipe@gmail.com"
    )
    endereco: str = Field(
        ...,
        max_length=45,
        description="Endereço do paciente",
        example="Rua 7 de Setembro, N10"
    )
    tipo_sanguineo: str = Field(
        ...,
        description="Tipo sanguíneo do paciente",
        example="O+"
    )
    observacoes: str = Field(
        ...,
        description="Observações sobre o paciente",
        example=""
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Felipe Fernando Corrêa",
                    "telefone": "(99) 99999-9999",
                    "cpf": "999.999.999-99",
                    "data_nascimento": "1999-02-13",
                    "email": "felipe@gmail.com",
                    "endereco": "Rua 7 de Setembro, N10",
                    "tipo_sanguineo": "O+",
                    "observacoes": ""
                }
            ]
        }
    }


class PacienteAlterarRequest(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nome completo do paciente",
        example="Felipe Fernando Corrêa"
    )
    telefone: str = Field(
        ...,
        max_length=15,
        description="Telefone do paciente",
        example="(99) 99999-9999"
    )
    email: str = Field(
        ...,
        description="Email do paciente",
        example="felipe@gmail.com"
    )
    endereco: str = Field(
        ...,
        description="Endereço do paciente",
        example="Rua 7 de Setembro, N10"
    )
    observacoes: str = Field(
        ...,
        description="Observações sobre o paciente",
        example=""
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Felipe Fernando Corrêa",
                    "telefone": "(99) 99999-9999",
                    "email": "felipe@gmail.com",
                    "endereco": "Rua 7 de Setembro, N10",
                    "observacoes": ""
                }
            ]
        }
    }


class PacienteResponse(BaseModel):
    id: UUID = Field(
        ...,
        description="Identificador único do paciente",
        example="e35f34e2-019c-49b9-bff2-43029aae5de6"
    )
    nome: str = Field(
        ...,
        description="Nome completo do paciente",
        example="Felipe Fernando Corrêa"
    )
    telefone: str = Field(
        ...,
        description="Telefone do paciente",
        example="(99) 99999-9999"
    )
    cpf: str = Field(
        ...,
        description="CPF do paciente",
        example="999.999.999-99"
    )
    data_nascimento: datetime = Field(
        ...,
        description="Data de nascimento do paciente",
        example="1999-02-13"
    )
    email: str = Field(
        ...,
        max_length=60,
        description="Email do paciente",
        example="felipe@gmail.com"
    )
    endereco: str = Field(
        ...,
        max_length=45,
        description="Endereço do paciente",
        example="Rua 7 de Setembro, N10"
    )
    tipo_sanguineo: str = Field(
        ...,
        description="Tipo sanguíneo do paciente",
        example="O+"
    )
    observacoes: str = Field(
        ...,
        description="Observações sobre o paciente",
        example=""
    )
    criado_em: datetime = Field(
        ...,
        description="Data e hora de criação do registro",
        example="2026-02-10T07:45:00"
    )
    alterado_em: datetime | None = Field(
        None,
        description="Data e hora da última alteração do registro",
        example="2026-02-10T07:45:00"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "e35f34e2-019c-49b9-bff2-43029aae5de6",
                    "nome": "Felipe Fernando Corrêa",
                    "telefone": "(99) 99999-9999",
                    "cpf": "999.999.999-99",
                    "data_nascimento": "1999-02-13",
                    "email": "felipe@gmail.com",
                    "endereco": "Rua 7 de Setembro, N10",
                    "tipo_sanguineo": "O+",
                    "observacoes": "",
                    "criado_em": "2026-02-10T07:45:00",
                    "alterado_em": None
                }
            ]
        }
    }
