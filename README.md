# Tratamento de dados - Escola de Artes Marciais

Primeira versão do tratamento de dados para o projeto de gestão de uma escola de artes marciais. O código foi desenvolvido em Python com Pandas e executado no Google Colab.

A escola ainda não tem uma base digital. Por isso, usamos **dados fictícios** para testar a limpeza, a organização dos cadastros, os pagamentos e a frequência.

## Arquivos

- `Escola_Artes_Marciais_Colab.ipynb`: notebook com o código.
- `Base_Escola.csv`: dados usados no teste.
- `dados_tratados.csv`: registros aproveitados depois do tratamento.
- `correcoes.csv`: alterações nos campos.
- `rejeitados.csv`: registros com erros e seus motivos.
- `resumo.txt`: total de registros e situação dos pagamentos.

Os quatro últimos arquivos são criados na pasta `resultados` quando o notebook é executado.

## Tratamento realizado

- Remoção de espaços extras e padronização de nomes, modalidades e turmas.
- Conversão de valores de mensalidade e datas.
- Identificação de campos vazios, valores inválidos e IDs repetidos.
- Separação dos registros válidos e rejeitados.
- Classificação das mensalidades e cálculo de frequência.

## Resultado do teste

| Descrição | Quantidade |
|---|---:|
| Registros lidos | 1.652 |
| Registros aproveitados | 1.484 |
| Registros rejeitados | 168 |
| Registros com correções | 878 |
| Campos corrigidos | 1.259 |
| Mensalidades pagas | 721 |
| Em aberto | 376 |
| Atrasadas | 387 |

A data de referência do teste é **02/11/2026**. A multa de 2% e a frequência mínima de 75% são valores provisórios, ainda não confirmados com a escola. A frequência serve para apoiar a avaliação de graduação, sem trocar a faixa automaticamente.
