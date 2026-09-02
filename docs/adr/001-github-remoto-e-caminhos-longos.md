# ADR-001 — GitHub como referência de sincronização e suporte a caminhos longos

- Status: Aceita
- Data: 2026-09-02

## Contexto

O repositório local apresentou arquivos simultaneamente marcados para exclusão e não rastreados. O remoto `DungeonCodes/planner_zoom_education` continha o histórico que deveria prevalecer. Três arquivos do acervo excederam o limite de comprimento de caminho do Windows.

## Decisão

Usar `origin/main` no GitHub como referência para recuperar o índice local e habilitar `core.longpaths=true` neste repositório.

## Consequências

O diretório local foi alinhado ao commit remoto sem perda dos arquivos e o GitHub Desktop pode abrir o repositório existente. Caminhos longos do acervo devem continuar sendo tratados por este repositório com suporte habilitado.
