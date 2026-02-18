"""
Modelo ORM para a tabela de profissionais.

Mapeia a entidade Profissional para a tabela 'profissionais' no PostgreSQL.
"""

from sqlalchemy import Column, String
from bem_saude.infraestrutura.banco_dados.modelos.modelo_base import ModeloBase
from sqlalchemy.dialects.postgresql import UUID


class ModeloProfissional(ModeloBase):
    """
    Modelo ORM da tabela 'profissionais'

    Mapeia os campos da entidade de domínio Profissional para colunas
    do banco de dados PostgreSQL.
    """
    __tablename__ = "profissionais"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )
    nome = Column(String(255), nullable=False)
    especialidade = Column(String(50), nullable=False)
    registro = Column(String(20), nullable=False, unique=True)
    duracao = Column(String(10), nullable=False)
    valor = Column(String(15), nullable=True)
    dias_semana = Column(String(100), nullable=True)
    status = Column(String(10), nullable=False)
