import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from bem_saude.api.configuracoes import configuracoes
from bem_saude.api.rotas.recepcionista_rotas import router as recepcionista_router
from bem_saude.api.rotas.paciente_rotas import router as paciente_router
from bem_saude.infraestrutura.banco_dados.conexao import engine
from bem_saude.infraestrutura.banco_dados.modelos.modelo_base import Base


logging.basicConfig(
    level=configuracoes.LOG_LEVEL,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H-%M-%S",
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Iniciando aplicação")
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.error(f"Erro ao criar tabelas: {e}")
    yield
    logger.info("Aplicação encerrando")


def criar_aplicacao() -> FastAPI:
    if configuracoes.eh_producao:
        logger.info("Iniciando aplicação em modo PRODUÇÃO")
        app = FastAPI(
            lifespan=lifespan,
            docs_url=None,
            redoc_url=None,
            openapi_url=None,
        )
    else:
        logger.info("Iniciando aplicação em modo DESENVOLVIMENTO")
        app = FastAPI(
            lifespan=lifespan,
            title="Bem Saúde API",
            version="1.0.0",
            docs_url="/docs",
            redoc_url="/redoc",
            openapi_url="/openapi.json",
        )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:4200",
            "http://bemsaude.com.br",
        ],
        allow_credentials=False,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )

    app.include_router(recepcionista_router)
    app.include_router(paciente_router)

    @app.get("/health")
    def health_check():
        return {
            "status": "ok",
            "ambiente": configuracoes.AMBIENTE,
            "swagger_habilitado": configuracoes.swagger_habilitado,
        }

    return app


app = criar_aplicacao()