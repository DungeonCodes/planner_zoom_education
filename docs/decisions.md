# Decisions

## Registro

Data: 2026-09-01
Decisão: Iniciar o projeto pelo recorte de Pensamento Computacional da Zoom Education para o Ensino Fundamental 1, do 1º ao 5º ano.
Motivo: Definição inicial do escopo do projeto.
Alternativas consideradas: Não definidas.
Impacto esperado: Direcionar a futura coleta e organização de materiais autorizados.

## Registro

Data: 2026-09-01
Decisão: Estruturar o cronograma pedagógico sem atribuir datas reais.
Motivo: O calendário letivo, a data inicial e a distribuição entre Semana A e Semana B ainda não foram definidos.
Alternativas consideradas: Preencher datas estimadas; descartada para não introduzir suposições.
Impacto esperado: Permitir o preenchimento posterior do calendário sem alterar a grade semanal.

## ADRs vigentes

A partir de 02/09/2026, as decisões duráveis do projeto são registradas em [docs/adr/README.md](adr/README.md). Os registros acima foram preservados como histórico anterior.

Em 14/09/2026, a extensão provisória do planejamento à Educação Infantil foi registrada no [ADR-014](adr/014-planejamento-infantil-set-dez-2026.md).

A grade semanal do Infantil fornecida pelo usuário foi registrada no [ADR-015](adr/015-grade-semanal-educacao-infantil-2026.md).

## Instrução operacional do usuário — 06/10/2026

Separar todo o acervo de semanários em `docs/semanarios/md/<segmento>/<mês>/` e `docs/semanarios/docx/<segmento>/<mês>/`, com MD como fonte de verdade e DOCX derivado. Fontes recebidas ficam preservadas em `data/`. O horizonte do Infantil nesta execução termina em 15/12, com dias úteis e somente os feriados oficiais informados. A instrução substitui os caminhos e o limite operacional anteriores sem editar ADRs ou refazer o planejamento do Fundamental I. Ver [manifesto](semanarios/migracao-2026-10-06.md).

## Ajuste autorizado do alinhamento quinzenal — 06/10/2026

Aplicar pontualmente os ADRs 004/011/012 ao planejamento futuro: preservar a Máquina GBC realizada pelo 4.ºC em 24/09, aprofundá-la em 08/10 pelo material existente e reconvergir em Q2; usar encontros semanais do 4.ºA para etapas da experiência essencial; especificar Colheitadeira no 3.ºD em 01/12; corrigir apenas os rótulos da maquete do 5.ºA/5.ºB. Decisão solicitada expressamente pelo usuário após auditoria; não altera ADRs, 1.º/2.º anos ou a sequência do 5.º. Ver [validação dos ajustes](semanarios/validacao-alinhamento-quinzenal-fundamental-1-2026-10-06.md).
