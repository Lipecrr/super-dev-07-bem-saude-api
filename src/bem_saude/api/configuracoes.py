"""
Modulo de configuracoes da aplicação
Carrega variaveis de ambiente usando Pydantic Settings
"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Configuracoes(BaseSettings):
    """
    Classe de configurações da aplicação.

    Carregar varaveis de ambiente do arquivo .env ou do ambiente do sistema.
    Todas as configurações necessarias para o funcionamento da aplicação devem
    ser definidas aqui
    """

    # Configuração do banco de dados
    # Formato: postgresql+psycopg://usuario:senha@host:porta/banco
    DATABASE_URL: str

    # Controla se o Swagger será habilitado e outros comportamentos
    AMBIENTE: str = "dev"

    # Nivel de loggine (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        # Buscar o .env na raiz do projeto
        env_file=str(Path(__file__).parent.parent.parent.parent / ".env"),
        env_file_encoding="utf-8",
        case_sesitive=False
    )

    @property
    def eh_producao(self) -> bool:
        return self.AMBIENTE.lower() == "prod" 
    @property
    def swagger_habilitado(self) -> bool:
        return not self.eh_producao

configuracoes = Configuracoes()