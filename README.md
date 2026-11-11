# Tratamento de dados — Escola de Artes Marciais

Projeto da disciplina de análise de dados, desenvolvido em Python com Pandas e executado no Google Colab. O trabalho parte do levantamento realizado em uma escola de artes marciais de Teresina, que ainda não possui um sistema de gestão.

Como a escola não tinha uma base digital disponível, utilizamos **dados fictícios** para testar o tratamento de cadastros, pagamentos e frequência. Os resultados não descrevem a situação real da escola.

## Integrantes 

|[Ronald Machado Guimarães de Sousa]|
|[João Victor Martins Freitas]| 
|[João Victor da Cunha Oliveira]|
|[Pedro Henrique Dias Carneiro Matos Silva]|
|[Artur Oliveira Santos Pereira]|
|[Luiz Eduardo Rios Barradas]|

## Arquivos do projeto

| Arquivo | Conteúdo |
|---|---|
| [`Entrega_Final_Artes_Marciais.ipynb`](Entrega_Final_Artes_Marciais.ipynb) | Algoritmo final e verificações de consistência |
| `Base_Escola.csv` | Base fictícia de entrada, com 1.652 registros |
| [`ANALISE_FINAL.md`](ANALISE_FINAL.md) | Interpretação dos dados e resultados do teste |
| [`DICIONARIO_DADOS.md`](DICIONARIO_DADOS.md) | Campos da base e dos arquivos gerados |
| [`MODELO_DADOS_FINAL.md`](MODELO_DADOS_FINAL.md) | Organização e relacionamento dos dados |
| `*_final.csv` | Dados tratados, correções, rejeições e tabelas organizadas |
| `baixa_manual_exemplo.csv` | Exemplo isolado de confirmação de pagamento |
| `resumo_final.txt` | Totais da execução |

Os arquivos com `parcial` no nome são da entrega anterior e foram mantidos para registrar a evolução do trabalho.

## Como executar

1. Abra o [Google Colab](https://colab.research.google.com/).
2. Em **Arquivo > Fazer upload de notebook**, selecione `Entrega_Final_Artes_Marciais.ipynb`.
3. Envie `Base_Escola.csv` na barra lateral **Arquivos** do Colab.
4. Execute as células de cima para baixo.
5. Os resultados serão salvos na pasta de trabalho do Colab, com os mesmos nomes dos arquivos finais publicados aqui.

O código utiliza Python e Pandas. A data de referência está fixada em **02/11/2026** para que o resultado seja sempre o mesmo.

## O que foi feito

- Padronização de nomes, modalidades, turmas, faixas, valores e datas.
- Identificação de campos obrigatórios ausentes, registros duplicados e valores inválidos.
- Separação dos registros aproveitados, rejeitados e corrigidos.
- Classificação das mensalidades em `Pago`, `Em aberto` e `Atrasado`.
- Cálculo de dias de atraso e multa de exemplo para cobranças vencidas e não pagas.
- Cálculo da frequência e indicação de quem atingiu o percentual definido para o teste de graduação.
- Organização dos resultados em tabelas de alunos, turmas, planos, pagamentos, frequência e graduação.
- Demonstração de baixa manual de um pagamento, em uma cópia da tabela.
- Execução de **12 verificações de consistência**.

## Resumo da execução

| Indicador | Total |
|---|---:|
| Registros recebidos | 1.652 |
| Aproveitados | 1.484 |
| Rejeitados | 168 |
| Registros corrigidos | 878 |
| Campos corrigidos | 1.259 |
| Mensalidades com pagamento registrado | 721 |
| Em aberto | 376 |
| Atrasadas | 387 |
| Atingiram a frequência mínima de teste | 741 |

O percentual de **75% de frequência** e a **multa de 2%** são parâmetros usados apenas para testar as regras. Eles ainda precisam ser confirmados com o proprietário. A frequência não altera a faixa do aluno automaticamente.

## Base fictícia e uso de IA

A base `Base_Escola.csv` foi criada com auxílio de IA, porque não havia registros digitais disponíveis para os testes. O texto abaixo resume as instruções utilizadas;

> Gerar uma base fictícia em CSV para uma escola de artes marciais, com 1.000 a 2.000 registros de alunos. Incluir identificação, nome, modalidade, turma, faixa, mensalidade, vencimento, pagamento e frequência. Variar os valores e inserir alguns campos vazios, repetições e inconsistências para testar a limpeza e a padronização com Python e Pandas.

