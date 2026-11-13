import json
movimentacoes = []

def salvar_movimentacoes():
    with open('movimentacoes.json', 'w', encoding='utf-8') as arquivo:
        json.dump(movimentacoes, arquivo, indent=4, ensure_ascii=False)

def carregar_movimentacoes():
    global movimentacoes
    try:
        with open('movimentacoes.json', 'r', encoding='utf-8') as arquivo:
            movimentacoes = json.load(arquivo)
    except FileNotFoundError:
        movimentacoes = []
    except json.JSONDecodeError:
        movimentacoes = []

def cadastrar_movimentacao(tipo):
    descricao = input(f'Digite a descrição da {tipo}: ').strip()
    if descricao == '':
        print('Não foi digitada uma descrição.')
        return
    try:
        valor = float(input(f'Digite o valor da {tipo}: '))
        if valor <= 0:
            print('O valor deve ser maior que zero.')
            return
        categoria = input('Digite a categoria: ').strip()
        if categoria == '':
            print('Não foi digitada uma categoria')
            return
        movimentacoes.append({
            'tipo': tipo,
            'descricao': descricao,
            'valor': valor,
            'categoria': categoria
        })
        salvar_movimentacoes()
        print(f'{tipo} cadastrada com sucesso!')
    except ValueError:
        print('Você não digitou um valor válido.')
        return

def listar_movimentacoes():
    print('\nÁrea de listagem de movimentações')
    if movimentacoes:
        for movimentacao in movimentacoes:
            print(f"{movimentacao['tipo']} - {movimentacao['descricao']} - {movimentacao['categoria']} - R$ {movimentacao['valor']:.2f}")
    else:
        print('Nenhuma movimentação cadastrada.')

def calcular_saldo():
    total_receitas = 0
    total_despesas = 0
    for movimento in movimentacoes:
        if movimento['tipo'] == 'receita':
            total_receitas += movimento['valor']
        elif movimento['tipo'] == 'despesa':
            total_despesas += movimento['valor']
    saldo_final = total_receitas - total_despesas

    print(f'Total Receitas: R$ {total_receitas:.2f}')
    print(f'Total Despesas: R$ {total_despesas:.2f}')
    print(f'Saldo Final: R$ {saldo_final:.2f}')

carregar_movimentacoes()

while True:

    print('\n=== CONTROLE FINANCEIRO ===')
    print('1 - Cadastrar Receita\n2 - Cadastrar Despesa\n3 - Listar Movimentações\n4 - Mostrar Saldo\n5 - Sair')

    try:
        escolha = int(input('Escolha uma opção: '))
    except ValueError:
        print('Você digitou um caractere inválido!')
        continue

    match escolha:
        case 1:
            cadastrar_movimentacao('receita')
        case 2:
            cadastrar_movimentacao('despesa')
        case 3:
            listar_movimentacoes()
        case 4:
            calcular_saldo()
        case 5:
            print(f'Encerrando o programa :)')
            break
        case _:
            print('Opção inválida. Tente novamente\n')

