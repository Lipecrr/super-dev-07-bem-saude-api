from uuid import UUID
from bem_saude.dominio.enums.status_cadastro import StatusCadastro
from bem_saude.infraestrutura.banco_dados.modelos.modelo_profissional import ModeloProfissional

from sqlalchemy.orm import Session


class RepositorioProfissional:
    def __init__(self, sessao: Session):
        self.sessao = sessao

    def criar(self, profissional: ModeloProfissional) -> ModeloProfissional:
        self.sessao.add(profissional)
        self.sessao.commit()
        self.sessao.flush(profissional)
        return profissional

    def listar(self) -> list[ModeloProfissional]:
        modelos = self.sessao.query(ModeloProfissional).order_by(ModeloProfissional.status, ModeloProfissional.nome).all()
        return modelos

    def buscar_por_id(self, id: UUID) -> ModeloProfissional | None:
        modelo = self.sessao.query(ModeloProfissional).filter(ModeloProfissional.id == id).first()
        return modelo

    def editar(self, id: UUID, nome: str, especialidade: str, duracao: str, valor: str, dias_semana: str):
        modelo = self.sessao.query(ModeloProfissional).filter(ModeloProfissional.id == id).first()
        if not modelo:
            return False

        modelo.nome = nome
        modelo.especialidade = especialidade
        modelo.duracao = duracao
        modelo.valor = valor
        modelo.dias_semana = dias_semana
        self.sessao.commit()
        return True

    def remover(self, id: UUID):
        modelo = self.sessao.query(ModeloProfissional).filter(ModeloProfissional.id == id).first()
        if not modelo:
            return False

        modelo.status = StatusCadastro.INATIVO.value
        self.sessao.commit()
        return True

    def ativar(self, id: UUID):
        modelo = self.sessao.query(ModeloProfissional).filter(ModeloProfissional.id == id).first()
        if not modelo:
            return False

        modelo.status = StatusCadastro.ATIVO.value
        self.sessao.commit()
        return True
