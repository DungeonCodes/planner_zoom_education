# Semanários

**Markdown é a fonte de verdade. DOCX é artefato derivado do seu Markdown.**

Fluxo: fontes → ADRs → planejamento → Markdown → validação → DOCX → QA visual. Havendo divergência, corrigir o derivado pelo Markdown, sem decidir conteúdo pedagógico pelo Word.

## Organização

```text
docs/semanarios/
├── md/
│   ├── fundamental-1/{2026-06,2026-08,2026-09,2026-10,2026-11,2026-12}/
│   └── infantil/{2026-08,2026-09,2026-10,2026-11,2026-12}/
├── docx/
│   ├── fundamental-1/{2026-06,2026-08,2026-09,2026-10,2026-11,2026-12}/
│   └── infantil/{2026-08,2026-09,2026-10,2026-11,2026-12}/
├── README.md
├── matriz-validacao-md-docx.md
├── migracao-2026-10-06.md
├── relatorio-infantil-e-migracao-2026-10-06.md
├── validacao-md-docx-2026-10-05-a-12-15.md
└── resumo-materiais-e-impressoes-2026-09.{md,docx}
```

A convenção foi solicitada pelo usuário em 06/10/2026 e substitui operacionalmente os caminhos de novos semanários citados nos ADRs 013–014. Os ADRs permanecem íntegros; suas regras pedagógicas continuam aplicadas. O [manifesto](migracao-2026-10-06.md) relaciona caminhos antigos e atuais. Não criar cópias ou atalhos de semanários nas pastas antigas.

Os históricos convertidos de junho e agosto também estão em `md/<segmento>/<mês>/`, sem reescrita pedagógica. Os Word recebidos são **fontes originais**, preservadas em `data/semanarios_prof_anterior/`, e não artefatos derivados nem fontes de decisão nova. Os DOCX nas raízes de entrega são derivados dos MD. Os READMEs de origem em `outputs/semanarios_prof_anterior/` permanecem como índices de proveniência. Documentação administrativa permanece nesta raiz, fora das raízes de semanários.

## Infantil

A [grade atual](../cronograma_pedagogico/grade_infantil_2026.md) confirma nove turmas em oito horários semanais de 50 minutos. Inf. 3B/3C compartilha quarta às 14:35. **O Infantil não usa ciclos A/B.** O [Plano Mestre](../cronograma_pedagogico/plano_mestre_infantil_2026-10-06-a-12-15.md) cobre 91 participações de turma em 81 horários reais, desde 06/10 até 15/12. As aulas de setembro foram confirmadas integralmente em 06/10, incluindo a 3C.

Os quatro semanários de outubro existentes foram aproveitados e sete novos de novembro/dezembro completam o horizonte. Inf. 4B encerra em 15/12; as turmas de quarta em 09/12 e 2A em 10/12. O [plano curricular](../cronograma_pedagogico/plano_infantil_set-dez_2026.md) registra os recortes e a progressão.

## Ferramentas e gates

`scripts/semanarios_paths.py` centraliza `MD_ROOT` e `DOCX_ROOT`. Instalar `scripts/requirements-semanarios.txt` em ambiente Python isolado. Executar da raiz do repositório:

```powershell
python scripts/semanarios.py validate --out-report .tmp/md-validado.json
python scripts/semanarios.py export --segmento infantil
python scripts/semanarios.py matrix
```

O exportador valida **todos os Markdown antes de escrever qualquer DOCX**. Texto, tabelas e listas vêm do MD; o Word anterior não fornece conteúdo. Os derivados usam A4, margens de 2,54 cm, títulos, cabeçalhos de tabela repetidos e paginação. A exportação não aprova o visual: renderizar e inspecionar todas as páginas antes da entrega. A [matriz](matriz-validacao-md-docx.md) compara texto visível e integridade dos pares; o QA desta execução está no [relatório](relatorio-infantil-e-migracao-2026-10-06.md).

## Fundamental I e preparo

O planejamento pedagógico de Rafael Martins e Ricardo Palhares até 15/12 não foi refeito. A mesma aula oficial continua compartilhada por série e semana, conforme ADR-011. Na migração de 06/10, os 21 pares futuros foram somente movidos. Posteriormente, por solicitação do usuário após a auditoria quinzenal, dez pares receberam ajustes pontuais: equalização do 4.ºC, etapas semanais do 4.ºA, especificação da retomada do 3.ºD e rótulos de continuidade do 5.ºA/5.ºB. Ver [validação e QA dos ajustes](validacao-alinhamento-quinzenal-fundamental-1-2026-10-06.md). Um DOCX histórico de 21–25/09 foi sincronizado com seu MD preexistente, que não sofreu alteração pedagógica.

Previsão de preparo do Fundamental I: cinco horas por semana completa, com uma hora adicional recomendada para testes, impressões e ajustes. Ver [simulação de preparo](../simulacoes/preparo-de-aulas-set-dez-2026.md).

## Resumo do Encontro

Cada roteiro conserva a mensagem de rotina para as famílias. O texto é uma previsão: conferir o que ocorreu e as adaptações antes de compartilhar. Não tratar mensagens no passado como prova de execução futura.
