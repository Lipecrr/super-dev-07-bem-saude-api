"""
Modelo ORM para a tabela de recepcionistas.

Mapeia a entidade Recepcionista para a tabela 'recepcionistas' no PostgreSQL.
"""

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from bem_saude.infraestrutura.banco_dados.modelos.modelo_base import ModeloBase


class ModeloRecepcionista(ModeloBase):
    """
    Modelo ORM da tabela 'recepcionistas'

    Mapeia os campos da entidade de domínio Recepcionista para colunas
    do banco de dados PostgreSQL.
    """

    __tablename__ = "recepcionistas"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
    )

    nome = Column(String(45), nullable=False)
    
    status = Column(String(10), nullable=False)