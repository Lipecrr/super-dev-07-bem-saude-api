# Sistema Bem Saúde

# Funcionalidades do Sistema:


## Status das consultas
- Agendada é quando a consulta é cadastrada
- Atrasada é uma tarefa (no back-end) que será executada minuto a minuto pegando as consultas do dia e atualizam quando passar do horário previsto
- Confirmada é quando foi realizado o check-in(paciente chegou na clínica)
- Cancelada é quando o paciente solicitou o cancelamento e/ou passou de 30m do horário previsto
- Em andamento é quando o médico iniciou a consulta
- Finalizada é quando o médico encerra a consutla


## Pacientes
- [Admin][Médico][Recepcionista] Listar os pacientes
- [Recepcionista] Cadastrar o paciente
    - Escolher a especialidade primeiro e depois 
- [Recepcionista] Editar os pacientes
- [Recepcionista] Inativar o paciente
- [Recepcionista] Ativar o paciente

## Profissionais (Médicos)
- [Admin][Recepcionista] Listar os médicos
- [Admin] Cadastrar o médico
- [Admin] Editar os médico
- [Admin] Inativar o médico
- [Admin] Ativar o médico

## Consultas
- [Admin][Recepcionista] Listar todas as consultas de todos os médicos
- [Médico] Listar todas as consultas do médico logado
- [Recepcionista] Cadastrar consulta
    - Não permitir cadastrar quando o paciente está inativado
    - Não permitir cadastrar uma consulta para médico que já tem atendimento naquela janela de atendimento
    - Não permitir cadastrar uma consulta para o mesmo paciente com médicos diferentes no mesmo horário e dia
- [Médico] Iniciar Consulta
    - Não permitir iniciar uma consulta enquanto outra estiver em andamento
- [Recepcionista] Cancelar um consulta de acordo com janela de cancelamento*¹
    - Gerar um fatura de cobrança quando o tempo para consulta for menor que a janela de cancelamento definida na tela de configurações
    - Não gerar cobrança quando o tempo para consulta for maior ou igual a janela de cancelamento 

## Check-in
- [Recepcionista] Listar as consultas disponíveis para check-in dos pacientes
    - Listar as consultas dos dia disponíveis para consulta
- [Recepcionista] Fazer o check-in do paciente
    - Não permitir fazer check-in antes de 30m da consulta
    - Não permitir fazer check-in após 5m do horário previsto da consulta
    - Não permitir fazer check-in de paciente inativado

## Consultas
- [Médico] Listas as consultas do médico
    - Ao abrir a tela de consultas deve retornar a lista de consultas do dia
    - Deve permitir filtrar por dia as consultas
- [Médico] Permitir iniciar a consulta
    - Não permitir iniciar a consulta fora do horário de atendimento
    - QUando inciiar a consulta deve redirecionar para a tela de atendimento


## Atendimento
- [Médico] Definir as anotações da consulta
- [Médico] Finalizar a consulta
    - Não permitir finalizar quando o médico não preencheu as anotações da consulta

## Configurações
- [Admin] Definir o janela de cancelamento *¹


## Atendimento (Médico)
