"""
Ponto de entrada principal da aplicação

Este módulo é o entru point para dodar a aplicação com uvcorn.

Uso: 
    uvicorn bem_saude.principal:app --reload
Ou para produção:
    uvicorn bem_saude.principal:app --host 0.0.0.0 --port 8000
"""

from bem_saude.api.app import app

__all__ = ["app"]