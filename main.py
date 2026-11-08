
movimentacoes = []


def cadastrar_receita():
    print('\nÁrea de cadastro de receita')
    descricao = input('Digite a descrição da Receita: ')
    valor = float(input('Digite o valor da Receita: '))
    movimentacoes.append({
        'tipo': 'receita',
        'descricao': descricao,
        'valor': valor
    })
    print('Receita cadastrada com sucesso!')


def cadastrar_despesa():
    print('\nÁrea de cadastro de despesa')
    descricao = input('Digite a descrição da Despesa: ')
    valor = float(input('Digite o valor da Despesa: '))
    movimentacoes.append({
        'tipo': 'despesa',
        'descricao': descricao,
        'valor': valor
    })
    print('Despesa cadastrada com sucesso!')

def listar_movimentacoes():
    print('\nÁrea de listagem de movimentações')
    if movimentacoes:
        for movimentacao in movimentacoes:
            print(f"{movimentacao['tipo']} - {movimentacao['descricao']} - R$ {movimentacao['valor']:.2f}")
    else:
        print('Nenhuma movimentação cadastrada.')


while True:

    print('\n=== CONTROLE FINANCEIRO ===')
    print('1 - Cadastrar Receita\n2 - Cadastrar Despesa\n3 - Listar Movimentações\n4 - Sair')

    escolha = int(input('Escolha uma opção: '))

    match escolha:
        case 1:
            cadastrar_receita()
        case 2:
            cadastrar_despesa()
        case 3:
            listar_movimentacoes()
        case 4:
            print(f'Encerrando o programa :)')
            break
        case _:
            print('Opção inválida. Tente novamente\n')
    