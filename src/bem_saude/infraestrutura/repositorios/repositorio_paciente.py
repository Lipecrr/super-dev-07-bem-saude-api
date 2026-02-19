from uuid import UUID
from sqlalchemy.orm import Session
from bem_saude.infraestrutura.banco_dados.modelos.modelo_paciente import ModeloPaciente


class RepositorioPaciente:
    def __init__(self, sessao: Session):
        self.sessao = sessao


    def criar(self, paciente: ModeloPaciente) -> ModeloPaciente:
        self.sessao.add(paciente)
        self.sessao.commit()
        self.sessao.flush(paciente)

        return paciente
    

    def editar(
            self,
            id: UUID,
            nome: str,
            telefone: str,
            endereco: str,
            observacoes: str,
            email: str):
        modelo = self.sessao.query(ModeloPaciente).filter(ModeloPaciente.id == id).first()
        if not modelo:
            return False
        
        modelo.nome = nome
        modelo.telefone = telefone
        modelo.endereco = endereco
        modelo.observacoes = observacoes
        modelo.email = email

        self.sessao.commit()
        return True
    

    def inativar(self, id: UUID):
        paciente = self.sessao.query(ModeloPaciente).filter(ModeloPaciente.id == id).first()
        if not paciente:
            return False
        
        paciente.status = "INATIVO"
        self.sessao.commit()
        return True
    

    def ativar(self, id: UUID):
        paciente = self.sessao.query(ModeloPaciente).filter(ModeloPaciente.id == id).first()
        if not paciente:
            return False
        
        paciente.status = "ATIVO"
        self.sessao.commit()
        return True
    

    def listar(self) -> list[ModeloPaciente]:
        pacientes = self.sessao.query(ModeloPaciente).order_by(ModeloPaciente.status, ModeloPaciente.nome).all()

        return pacientes
    

    def buscar_por_id(self, id: UUID) -> ModeloPaciente | None:
        paciente = self.sessao.query(ModeloPaciente).filter(ModeloPaciente.id == id).first()
        if not paciente:
            return False
        
        return paciente