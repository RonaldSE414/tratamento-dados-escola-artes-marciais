# Análise final dos dados

**Escola de Artes Marciais — projeto de dados**  
**Data de referência:** 02/11/2026

## 1. Objetivo

O levantamento inicial mostrou que a escola não possui um sistema para acompanhar alunos, mensalidades e graduações. Como não existia uma base digital para utilizar no algoritmo, montamos uma base fictícia com auxílio de IA. A proposta foi testar como os registros poderiam ser limpos, organizados e classificados.

Esta análise apresenta os resultados obtidos com `Base_Escola.csv`. **Os números são de uma simulação e não representam os alunos ou as finanças da escola visitada.**

## 2. Qualidade dos dados

O arquivo de entrada tinha 1.652 registros. Depois da conferência dos campos, 1.484 foram aproveitados (89,8%) e 168 foram rejeitados (10,2%). Entre os registros aproveitados, 878 precisaram de alguma correção, totalizando 1.259 campos ajustados.

| Etapa | Registros |
|---|---:|
| Lidos | 1.652 |
| Aproveitados | 1.484 |
| Rejeitados | 168 |
| Aproveitados com correção | 878 |
| Campos corrigidos | 1.259 |

### Motivos das rejeições

| Motivo principal | Quantidade |
|---|---:|
| Campo obrigatório vazio | 51 |
| Aulas ou presenças inválidas | 29 |
| Identificador repetido | 21 |
| Número inválido | 17 |
| Data de pagamento futura | 15 |
| Modalidade não reconhecida | 13 |
| Valor da mensalidade inválido | 12 |
| Data inválida | 10 |
| **Total** | **168** |

O algoritmo registra um motivo principal para cada linha rejeitada, seguindo a ordem das validações. Portanto, uma linha com mais de um problema aparece apenas uma vez nessa contagem.

Os campos mais alterados foram `nome` (262), `valor_mensalidade` (241), `modalidade` (224), `turma` (188), `vencimento` (150), `faixa_atual` (129) e `data_pagamento` (65). As correções envolveram principalmente formatação de texto, valores e datas. Não foram inventados valores para completar cadastros inválidos.

Entre os 1.484 registros válidos, **763 ficaram sem data de pagamento**. Isso não é erro: são as 376 cobranças em aberto e as 387 atrasadas.

## 3. Distribuição por modalidade

| Modalidade | Registros |
|---|---:|
| Jiu-jitsu | 672 |
| Muay Thai | 445 |
| Judô | 247 |
| Karatê | 120 |
| **Total** | **1.484** |

A base gerou 72 combinações de modalidade e turma e 16 valores distintos de mensalidade. São categorias identificadas nos dados de teste, não a quantidade confirmada de turmas e planos reais da escola.

## 4. Situação dos pagamentos

| Situação | Registros | Percentual |
|---|---:|---:|
| Pago | 721 | 48,6% |
| Em aberto | 376 | 25,3% |
| Atrasado | 387 | 26,1% |
| **Total** | **1.484** | **100,0%** |

A classificação considera a data de referência de 02/11/2026. Um pagamento com data preenchida é classificado como pago; quando não há pagamento, a comparação com o vencimento indica se está em aberto ou atrasado.

Dos **721 pagamentos registrados**, 189 foram feitos após o vencimento. As **387 cobranças atrasadas e não pagas** somam R$ 50.985,00 na base fictícia. Aplicando a multa de teste de 2%, a estimativa seria de **R$ 1.019,70**. Não são valores efetivamente devidos à escola.

O notebook também calcula os dias de atraso. Uma função demonstra a baixa manual de uma cobrança atrasada: após informar a data de confirmação, a situação passa para `Pago`. O exemplo é salvo separadamente em `baixa_manual_exemplo.csv` e não altera os dados originais.

## 5. Frequência e graduação

A frequência foi calculada dividindo as presenças pela quantidade de aulas e multiplicando o resultado por 100.

| Indicador | Resultado |
|---|---:|
| Frequência média | 71,9% |
| Frequência mediana | 73,3% |
| Atingiram o mínimo de teste (75%) | 741 |
| Ficaram abaixo de 75% | 743 |

| Faixa de frequência | Registros |
|---|---:|
| Abaixo de 50% | 133 |
| De 50% a menos de 75% | 610 |
| De 75% a menos de 90% | 543 |
| De 90% a 100% | 198 |

O indicador mostra apenas quais cadastros atingiram o percentual utilizado na simulação. Ele **não aprova uma nova faixa**. A decisão depende da avaliação do professor e dos critérios que a escola ainda precisa confirmar.

## 6. Resultado da versão final

A entrega parcial tratava os dados em um arquivo consolidado. A versão final passou a separar as informações em arquivos de alunos, turmas, planos, pagamentos, frequência e graduação. Também foram incluídos os dias de atraso, a demonstração da baixa manual e **12 verificações de consistência** executadas no notebook.

O resultado mostra que o algoritmo consegue padronizar os registros, detectar inconsistências e produzir informações para apoiar a gestão. Antes de usar esse fluxo de verdade, seria preciso validar as regras com o proprietário, montar um histórico de pagamentos, registrar presenças por aula e implementar o banco de dados e o aplicativo planejados.

**Conclusão:** a análise permite avaliar o funcionamento do algoritmo com a base fictícia. Ela não permite concluir quantos alunos, pagamentos ou atrasos a escola real possui.
