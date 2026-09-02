# ADR-002 — Separação entre fontes originais e versões de leitura

- Status: Aceita
- Data: 2026-09-02

## Contexto

Semanários e horários recebidos são documentos internos de origem e precisam permanecer íntegros. Ao mesmo tempo, o planejamento exige leitura, busca e comparação rápida de seu conteúdo.

## Decisão

Armazenar os originais em `data/`, ignorada pelo Git, e gerar versões Markdown em `outputs/`:

- `data/semanarios_prof_anterior/` → `outputs/semanarios_prof_anterior/`;
- `data/horarios_aulas/` → `outputs/horarios_aulas/`.

## Consequências

Os arquivos fonte não são alterados nem publicados acidentalmente. As versões Markdown permitem auditoria, busca textual e uso direto no planejamento.
