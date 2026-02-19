"""
Modelo ORM para a tabela de pacientes.

Mapeia a entidade Recepcionista para a tabela 'pacientes' no PostgreSQL.
"""

from sqlalchemy import Column, String, Date, Text
from sqlalchemy.dialects.postgresql import UUID
from bem_saude.infraestrutura.banco_dados.modelos.modelo_base import ModeloBase


class ModeloPaciente(ModeloBase):
    __tablename__ = "pacientes"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    nome= Column(
        String(100),
        nullable=False
    )

    telefone= Column(
        String(15),
        nullable=False
    )

    cpf= Column(
        String(14),
        nullable=False
    )

    status= Column(
        String(10),
        nullable=False
    )

    email= Column(
        String(60),
        nullable=True
    )

    endereco= Column(
        String(45),
        nullable=True
    )

    data_nascimento= Column(
        Date,
        nullable=False
    )

    observacoes= Column(
        Text,
        nullable=True
    )

    tipo_sanguineo= Column(
        String(3),
        nullable=False
    )
