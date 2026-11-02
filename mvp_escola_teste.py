"""Tratamento inicial dos dados para o projeto da escola de artes marciais.

Os registros são simulados para testar a limpeza, os pagamentos e a frequência.
"""

import csv
from collections import Counter
from datetime import datetime, date
from pathlib import Path

ARQUIVO = Path('dados_escola_teste.csv')
SAIDA = Path('resultados')
HOJE = date(2026, 11, 2)  # data fixa para a demonstração
MULTA = 0.02             # só exemplo; falta confirmar com a escola
FREQUENCIA_MINIMA = 75   # só exemplo; não libera troca de faixa sozinho

MODALIDADES = {
    'jiu-jitsu': 'Jiu-jitsu', 'jiu jitsu': 'Jiu-jitsu',
    'muay thai': 'Muay Thai', 'judô': 'Judô', 'judo': 'Judô',
    'karatê': 'Karatê', 'karate': 'Karatê',
}


def ler_data(texto):
    # Aceita os dois jeitos de escrever uma data.
    for formato in ('%Y-%m-%d', '%d/%m/%Y'):
        try:
            return datetime.strptime(texto.strip(), formato).date()
        except ValueError:
            continue
    raise ValueError('data inválida')


def salvar_csv(caminho, linhas, colunas):
    with caminho.open('w', encoding='utf-8-sig', newline='') as arq:
        writer = csv.DictWriter(arq, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(linhas)


def processar(linha, ids):
    # Padroniza os textos antes de verificar cada cadastro.
    codigo = linha['id_aluno'].strip()
    nome = ' '.join(linha['nome'].strip().split()).title()
    modalidade_original = ' '.join(linha['modalidade'].strip().lower().split())
    modalidade = MODALIDADES.get(modalidade_original)
    turma = linha['turma'].strip().upper()
    faixa = ' '.join(linha['faixa_atual'].strip().split()).title()
    valor_txt = linha['valor_mensalidade'].strip().replace('R$', '').replace(' ', '')
    valor_txt = valor_txt.replace(',', '.')

    # Estes campos precisam de revisão quando estão errados.
    if not codigo or not nome or not turma or not faixa:
        raise ValueError('cadastro com campo obrigatório vazio')
    if codigo in ids:
        raise ValueError('identificador repetido')
    if not modalidade:
        raise ValueError('modalidade não reconhecida')
    try:
        valor = float(valor_txt)
        aulas = int(linha['quantidade_aulas'].strip())
        presencas = int(linha['presencas'].strip())
    except ValueError:
        raise ValueError('número inválido')
    if valor <= 0:
        raise ValueError('valor da mensalidade inválido')
    if aulas <= 0 or not (0 <= presencas <= aulas):
        raise ValueError('quantidade de aulas ou presenças inválida')

    try:
        vencimento = ler_data(linha['vencimento'])
        pagamento = ler_data(linha['data_pagamento']) if linha['data_pagamento'].strip() else None
    except ValueError:
        raise ValueError('data de vencimento ou pagamento inválida')
    if pagamento and pagamento > HOJE:
        raise ValueError('pagamento com data futura')

    # Guarda o antes e depois dos campos modificados.
    alteracoes = []
    corrigidos = {
        'nome': nome,
        'modalidade': modalidade,
        'turma': turma,
        'faixa_atual': faixa,
        'valor_mensalidade': f'{valor:.2f}',
        'vencimento': vencimento.isoformat(),
        'data_pagamento': pagamento.isoformat() if pagamento else '',
    }
    for campo, novo in corrigidos.items():
        if linha[campo] != novo:
            alteracoes.append({'campo': campo, 'antes': linha[campo], 'depois': novo})

    # Calcula a situação da mensalidade e o percentual de frequência.
    situacao = 'Pago' if pagamento else ('Atrasado' if vencimento < HOJE else 'Em aberto')
    percentual = round(presencas * 100 / aulas, 1)
    resultado = {
        'id_aluno': codigo, 'nome': nome, 'modalidade': modalidade,
        'turma': turma, 'faixa_atual': faixa,
        'valor_mensalidade': f'{valor:.2f}',
        'vencimento': vencimento.isoformat(),
        'data_pagamento': pagamento.isoformat() if pagamento else '',
        'situacao_pagamento': situacao,
        'multa_exemplo': f'{valor * MULTA:.2f}' if situacao == 'Atrasado' else '0.00',
        'quantidade_aulas': aulas, 'presencas': presencas,
        'frequencia_percentual': percentual,
        'frequencia_minima_atingida': 'Sim' if percentual >= FREQUENCIA_MINIMA else 'Não',
    }
    return resultado, alteracoes


def executar():
    if not ARQUIVO.exists():
        print('Envie o arquivo dados_escola_teste.csv para o Colab.')
        return
    organizados, rejeitados, correcoes = [], [], []
    ids = set()
    total = 0

    with ARQUIVO.open(encoding='utf-8-sig', newline='') as arq:
        for numero, linha in enumerate(csv.DictReader(arq), start=2):
            total += 1
            try:
                aluno, mudancas = processar(linha, ids)
                organizados.append(aluno)
                ids.add(aluno['id_aluno'])
                for mudanca in mudancas:
                    correcoes.append({'linha': numero, 'id_aluno': aluno['id_aluno'], **mudanca})
            except (ValueError, KeyError, TypeError) as erro:
                rejeitados.append({'linha': numero, 'id_aluno': linha.get('id_aluno', ''), 'motivo': str(erro)})

    SAIDA.mkdir(exist_ok=True)
    colunas = list(organizados[0]) if organizados else ['id_aluno']
    salvar_csv(SAIDA / 'dados_tratados.csv', organizados, colunas)
    salvar_csv(SAIDA / 'rejeitados.csv', rejeitados, ['linha', 'id_aluno', 'motivo'])
    salvar_csv(SAIDA / 'correcoes.csv', correcoes, ['linha', 'id_aluno', 'campo', 'antes', 'depois'])

    situacoes = Counter(a['situacao_pagamento'] for a in organizados)
    linhas_corrigidas = len(set(m['linha'] for m in correcoes))
    resumo = (
        'TRATAMENTO DA BASE DA ESCOLA - DADOS FICTÍCIOS\n'
        'Data do teste: 02/11/2026\n'
        f'Registros lidos: {total}\n'
        f'Registros aproveitados: {len(organizados)}\n'
        f'Registros com algum campo corrigido: {linhas_corrigidas}\n'
        f'Correções de campos: {len(correcoes)}\n'
        f'Registros rejeitados: {len(rejeitados)}\n'
        f'Mensalidades pagas: {situacoes["Pago"]}\n'
        f'Mensalidades em aberto: {situacoes["Em aberto"]}\n'
        f'Mensalidades atrasadas: {situacoes["Atrasado"]}\n'
        'Multa e frequência mínima são regras provisórias usadas apenas no teste.\n'
    )
    (SAIDA / 'resumo.txt').write_text(resumo, encoding='utf-8')
    print(resumo)
    print('Arquivos criados: dados_tratados.csv, correcoes.csv, rejeitados.csv e resumo.txt')


if __name__ == '__main__':
    executar()
