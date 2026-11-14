
# 🥋 Tratamento de Dados — Escola de Artes Marciais

**Projeto de Análise de Dados | Python + Pandas**

Este projeto apresenta o desenvolvimento de um algoritmo para limpeza, padronização e organização de dados de uma escola de artes marciais, utilizando Python e a biblioteca Pandas no Google Colab.

O trabalho foi desenvolvido a partir de um levantamento realizado em uma escola de Teresina. Como não havia uma base digital disponível, foi utilizada uma base fictícia para realizar os testes.

---

## 👥 Integrantes

- Ronald Machado Guimarães de Sousa
- João Victor Martins Freitas
- João Victor da Cunha Oliveira
- Pedro Henrique Dias Carneiro Matos Silva
- Artur Oliveira Santos Pereira
- Luiz Eduardo Rios Barradas

## 📁 Estrutura do repositório

```text
tratamento-dados-escola-artes-marciais/
│
├── entrega-parcial/
│   ├── Notebook da entrega parcial (.ipynb)
│   ├── dados_tratados_parcial.csv
│   ├── correcoes_parcial.csv
│   ├── rejeitados_parcial.csv
│   └── resumo_parcial.txt
│
├── entrega-final/
│   ├── Entrega_Final_Artes_Marciais.ipynb
│   ├── alunos_final.csv
│   ├── turmas_final.csv
│   ├── planos_final.csv
│   ├── pagamentos_final.csv
│   ├── frequencias_final.csv
│   ├── graduacoes_final.csv
│   ├── dados_tratados_final.csv
│   ├── correcoes_final.csv
│   ├── rejeitados_final.csv
│   ├── baixa_manual_exemplo.csv
│   └── resumo_final.txt
│
├── Base_Escola.csv
├── ANALISE_FINAL.md
├── DICIONARIO_DADOS.md
├── MODELO_DADOS_FINAL.md
└── README.md
```

## 📄 Arquivos do projeto

| Arquivo | Descrição |
|---|---|
| `Base_Escola.csv` | Base fictícia utilizada nos testes, com 1.652 registros |
| [Notebook final](entrega-final/Entrega_Final_Artes_Marciais.ipynb) | Algoritmo final desenvolvido em Python e Pandas |
| `dados_tratados_final.csv` | Registros aproveitados após o tratamento |
| `correcoes_final.csv` | Registro das correções realizadas |
| `rejeitados_final.csv` | Registros rejeitados e seus motivos |
| `alunos_final.csv` | Dados dos alunos organizados |
| `turmas_final.csv` | Identificação das turmas |
| `planos_final.csv` | Identificação dos planos e valores das mensalidades |
| `pagamentos_final.csv` | Situação dos pagamentos, vencimentos e atrasos |
| `frequencias_final.csv` | Dados de frequência dos alunos |
| `graduacoes_final.csv` | Indicadores para avaliação de graduação |
| `baixa_manual_exemplo.csv` | Demonstração de confirmação manual de pagamento |
| `resumo_final.txt` | Resumo dos resultados do processamento |

Os arquivos da entrega parcial estão na pasta `entrega-parcial/`, enquanto osda versão final estão organizados em `entrega-final/`.

## ⚙️ Desenvolvimento

O algoritmo realiza o tratamento dos cadastros, identifica registros inválidos, registra correções e organiza os dados para análise.

Na versão final, foram acrescentados:

- Organização das informações em tabelas relacionadas.
- Classificação dos pagamentos e cálculo de atrasos.
- Cálculo da frequência dos alunos.
- Indicadores para avaliação de graduação.
- Exemplo de baixa manual de pagamento.
- 12 verificações de consistência.

## 📊 Resultados

| Indicador | Quantidade |
|---|---:|
| Registros analisados | 1.652 |
| Registros aproveitados | 1.484 |
| Registros rejeitados | 168 |
| Registros com correções | 878 |
| Campos corrigidos | 1.259 |
| Pagamentos registrados | 721 |
| Pagamentos em aberto | 376 |
| Pagamentos atrasados | 387 |

Os resultados foram obtidos com dados fictícios. A multa de 2% e a frequência mínima de 75% foram utilizadas como parâmetros de teste.

## 🤖 Base fictícia e prompt utilizado

A base `Base_Escola.csv` foi criada com auxílio de inteligência artificial, conforme a proposta apresentada à professora, para permitir os testes do algoritmo.

**Prompt utilizado:**

> Gerar uma base fictícia em CSV para uma escola de artes marciais, com 1.000 a 2.000 registros de alunos. Incluir identificação, nome, modalidade, turma, faixa, mensalidade, vencimento, pagamento e frequência. Variar os valores e inserir alguns campos vazios, repetições e com inconsistências.

## 📚 Documentação

| Documento | Conteúdo |
|---|---|
| [Análise Final](ANALISE_FINAL.md) | Resultados e interpretação dos dados |
| [Dicionário de Dados](DICIONARIO_DADOS.md) | Descrição dos campos utilizados |
| [Modelo de Dados](MODELO_DADOS_FINAL.md) | Estrutura e relacionamento das tabelas |

## 💻 Execução

O projeto pode ser executado no [Google Colab](https://colab.research.google.com/).

1. Abra o [notebook final](entrega-final/Entrega_Final_Artes_Marciais.ipynb).
2. Carregue o arquivo `Base_Escola.csv`.
3. Execute as células em sequência.

Os arquivos CSV e o resumo da execução são gerados pelo próprio notebook.

---

**Ferramentas utilizadas:** Python • Pandas • Google Colab • GitHub
