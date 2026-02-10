from sqlalchemy import Boolean, Column, Date, String
from sqlalchemy.dialects.postgresql import UUID
from bem_saude.infraestrutura.banco_dados.modelos.modelo_base import ModeloBase


class ModeloPaciente(ModeloBase):
    __tablename__ = "pacientes"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )
    nome = Column(
        String(100),
        nullable=False
    )
    cpf = Column(
        String(14),
        nullable=False
    )
    data_nascimento = Column(
        Date,
        nullable=False
    )
    email = Column(
        String(60),
        nullable=False
    )
    endereco = Column(
        String(45),
        nullable=False
    )
    tipo_sanguineo = Column(
        String(3),
        nullable=False
    )
    observacoes= Column(
        String(200)
    )

    # status = Column(
    #     Boolean,
    #     nullable=False,
    #     default=True
    # )