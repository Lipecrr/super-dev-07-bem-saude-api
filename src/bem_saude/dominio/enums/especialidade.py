from enum import Enum


class Especialidade(str, Enum):
    CLINICO_GERAL = "Clínico Geral"
    CARDIOLOGIA = "Cardiologia"
    ORTOPEDIA = "Ortopedia"
    DERMATOLOGIA = "Dermatologia"
    PEDIATRIA = "Pediatria"
