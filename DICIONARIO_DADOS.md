# Dicionário de dados

Descrição dos campos utilizados na base fictícia e nos arquivos gerados pelo notebook final.

## Base de entrada — `Base_Escola.csv`

| Campo | Tipo | Regra e significado |
|---|---|---|
| `id_aluno` | Texto | Identificação obrigatória, sem repetição entre registros aceitos |
| `nome` | Texto | Nome do aluno; não pode ser vazio |
| `modalidade` | Texto | Jiu-jitsu, Muay Thai, Judô ou Karatê, após padronização |
| `turma` | Texto | Código obrigatório da turma |
| `faixa_atual` | Texto | Graduação informada no cadastro |
| `valor_mensalidade` | Decimal | Valor positivo, em reais |
| `vencimento` | Data | Data obrigatória da cobrança |
| `data_pagamento` | Data ou vazio | Vazia quando não há pagamento; datas futuras são rejeitadas no teste |
| `quantidade_aulas` | Inteiro | Total de aulas considerado, maior que zero |
| `presencas` | Inteiro | Número de presenças, entre zero e o total de aulas |

As datas são padronizadas para `AAAA-MM-DD`; valores monetários usam duas casas decimais. O código aceita datas de entrada nos formatos `AAAA-MM-DD` e `DD/MM/AAAA`.

## Dados tratados — `dados_tratados_final.csv`

Mantém os dez campos da entrada e acrescenta:

| Campo | Tipo | Significado |
|---|---|---|
| `situacao_pagamento` | Texto | `Pago`, `Em aberto` ou `Atrasado` |
| `multa_exemplo` | Decimal | 2% do valor vencido ainda não pago, somente para teste |
| `frequencia_percentual` | Decimal | Percentual de presenças, exibido com uma casa decimal |
| `frequencia_minima_atingida` | Texto (`Sim`/`Não`) | Verificação de 75% de frequência, sem trocar a faixa |

O percentual é comparado ao limite **antes do arredondamento** para evitar mudanças indevidas na classificação.

## Arquivos de saída

| Arquivo | Campos |
|---|---|
| `alunos_final.csv` | `id_aluno`, `nome`, `modalidade`, `id_turma`, `id_plano`, `faixa_atual` |
| `turmas_final.csv` | `id_turma`, `modalidade`, `turma` |
| `planos_final.csv` | `id_plano`, `valor_mensalidade` |
| `pagamentos_final.csv` | `id_pagamento`, `id_aluno`, `valor_mensalidade`, `vencimento`, `data_pagamento`, `situacao_pagamento`, `mes_referencia`, `dias_atraso`, `pago_apos_vencimento`, `multa_estimada`, `valor_estimado`, `confirmacao_manual` |
| `frequencias_final.csv` | `id_aluno`, `quantidade_aulas`, `presencas`, `frequencia_percentual` |
| `graduacoes_final.csv` | `id_aluno`, `faixa_atual`, `frequencia_percentual`, `atingiu_frequencia_minima`, `situacao` |
| `correcoes_final.csv` | `linha`, `id_aluno`, `campo`, `antes`, `depois` |
| `rejeitados_final.csv` | `linha`, `id_aluno`, `motivo` |
| `baixa_manual_exemplo.csv` | Mesmos campos de `pagamentos_final.csv`, contendo somente a cobrança usada na demonstração |

### Campos financeiros

- `mes_referencia`: ano e mês do vencimento (`AAAA-MM`). Não representa um histórico de vários meses por aluno.
- `dias_atraso`: dias entre o vencimento e a data de referência, para cobranças vencidas, ou entre vencimento e pagamento, se pago depois do prazo.
- `pago_apos_vencimento`: `Sim` ou `Não`, conforme a data do pagamento.
- `multa_estimada`: valor da multa de teste aplicada somente aos débitos em atraso e ainda não pagos.
- `valor_estimado`: mensalidade mais multa estimada, quando houver.
- `confirmacao_manual`: fica `Não` na tabela principal; no arquivo de demonstração muda para `Sim` após a função de baixa manual.

### Campos de graduação

- `atingiu_frequencia_minima`: `Sim` ou `Não` conforme o limite de teste de 75%.
- `situacao`: indica se a frequência permite encaminhar o aluno para avaliação; não há troca automática de faixa.

Os critérios de 2% de multa e 75% de frequência são provisórios. O CSV não contém dados de responsáveis, histórico de aulas por data, alterações de faixa ou comprovantes de pagamento.
