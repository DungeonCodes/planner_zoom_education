# ADR-007 — Skill reutilizável para criação de semanários

- Status: Aceita
- Data: 2026-09-02

## Contexto

O semanário precisa cruzar a grade A/B, o conteúdo confirmado de cada turma, as páginas do professor e do aluno, as restrições de calendário e as decisões pedagógicas. Repetir esse levantamento manualmente a cada semana aumenta o risco de inconsistência.

## Decisão

Criar a skill local `semanario-pedagogico` em `C:/Users/tisap/.codex/skills/semanario-pedagogico`. Ela contém um fluxo de consulta, regras de rastreabilidade e um modelo de semanário.

## Consequências

Novos semanários devem usar essa skill, por exemplo com `$semanario-pedagogico`. A skill preserva a necessidade de confirmar informações ausentes e não autoriza alteração da grade ou do currículo.
