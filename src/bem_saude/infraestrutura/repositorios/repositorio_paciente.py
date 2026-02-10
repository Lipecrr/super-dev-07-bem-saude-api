from uuid import UUID
from sqlalchemy.orm import Session
from bem_saude.infraestrutura.banco_dados.modelos.modelo_paciente import ModeloPaciente


class RepositorioPaciente:
    def __init__(self, sessao: Session):
        self.sessao = sessao


    def criar(self,paciente: ModeloPaciente) -> ModeloPaciente:
        self.sessao.add(paciente)
        self.sessao.commit()
        self.sessao.flush(paciente)

        return paciente
    

    def listar(self) -> list[ModeloPaciente]:
        modelos = self.sessao.query(ModeloPaciente).all()
        return modelos
    

    def remover(self, id: UUID):
        modelo = self.sessao.query(ModeloPaciente).filter(ModeloPaciente.id == id).first()
        if not modelo:
            return False
        
        modelo.status = "INATIVO"
        self.sessao.commit()
        return True
    

    def buscar_por_id(self, id: UUID) -> ModeloPaciente | None:
        modelo = self.sessao.query(ModeloPaciente).filter(ModeloPaciente.id == id).first()
        return modelo
    

    def editar(self, id: UUID, nome: str):
        modelo = self.sessao.query(ModeloPaciente).filter(ModeloPaciente.id == id).first()
        if not modelo:
            return False
        
        modelo.nome = nome
        self.sessao.commit()
        return True
