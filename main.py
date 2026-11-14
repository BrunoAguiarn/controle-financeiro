import json
import shutil
import os

movimentacoes = []
arquivo_valido = True

def salvar_movimentacoes():
    if not arquivo_valido:
        print('O arquivo de movimentações está corrompido.')
        return False
    with open('movimentacoes.json', 'w', encoding='utf-8') as arquivo:
        json.dump(movimentacoes, arquivo, indent=4, ensure_ascii=False)
    return True

def carregar_movimentacoes():
    global movimentacoes
    global arquivo_valido
    try:
        with open('movimentacoes.json', 'r', encoding='utf-8') as arquivo:
            movimentacoes = json.load(arquivo)
    except FileNotFoundError:
        movimentacoes = []
    except json.JSONDecodeError:
        print('Erro: o arquivo de movimentações está corrompido')
        print('Iniciando criação de backup...')
        if os.path.exists('movimentacoes_backup.json'):
            print('O backup já existe!')
        else:
            shutil.copy2('movimentacoes.json', 'movimentacoes_backup.json')
            print('Cópia de segurança criada com sucesso!')
        arquivo_valido = False
        movimentacoes = []

def cadastrar_movimentacao(tipo):
    print(f'\n=== CADASTRAR {tipo.upper()} ===')
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
        salvou = salvar_movimentacoes()
        if salvou:
            print(f'{tipo} cadastrada com sucesso!')
        else:
            movimentacoes.pop()
            print('A movimentação não foi salva')
    except ValueError:
        print('Você não digitou um valor válido.')
        return

def listar_movimentacoes():
    print('\n=== LISTAGEM DE MOVIMENTAÇÕES ===')
    if movimentacoes:
        for movimentacao in movimentacoes:
            print(f"{movimentacao['tipo']} - {movimentacao['descricao']} - {movimentacao['categoria']} - R$ {movimentacao['valor']:.2f}")
    else:
        print('Nenhuma movimentação cadastrada.')

def excluir_movimentacao():
    print('\n=== EXCLUIR MOVIMENTAÇÃO ===')
    if not movimentacoes:
        print('Nenhuma movimentação para excluir.')
        return
    for indice, movimento in enumerate(movimentacoes, start=1):
        print(f"{indice} - {movimento['tipo']} - {movimento['descricao']} - R${movimento['valor']:.2f}")
    try:
        indice = int(input('Digite o numero da movimentação que deseja excluir: ')) - 1
        if 0 <= indice < len(movimentacoes):
            confirma = (input('Confirma a exclusão? [S/N]: ').upper())
            if confirma == 'S':
                movimento = movimentacoes.pop(indice)
                salvou = salvar_movimentacoes()
                if salvou:
                    print(f"Movimentação '{movimento['descricao']}' foi excluida")
                    return
                print('Não foi possível salvar a alteração. A movimentação foi restaurada.')
                movimentacoes.insert(indice, movimento)
                return
            elif confirma == 'N':
                print('A exclusão foi cancelada')
                return
            else:
                print('Opção inválida')
                return
        print('A movimentação digitada não existe')
        
    except ValueError:
        print('Você não digitou um numero válido.')
        return

def calcular_saldo():
    total_receitas = 0
    total_despesas = 0
    for movimento in movimentacoes:
        if movimento['tipo'] == 'receita':
            total_receitas += movimento['valor']
        elif movimento['tipo'] == 'despesa':
            total_despesas += movimento['valor']
    saldo_final = total_receitas - total_despesas
    print('\n=== CONSULTAR SALDO ===')
    print(f'Total Receitas: R$ {total_receitas:.2f}')
    print(f'Total Despesas: R$ {total_despesas:.2f}')
    print(f'Saldo Final: R$ {saldo_final:.2f}')

carregar_movimentacoes()

while True:

    if not arquivo_valido:
        print('O programa será encerrado, verificar arquivo de movimentações manualmente.')
        break

    print('\n=== CONTROLE FINANCEIRO ===')
    print('1 - Cadastrar Receita\n2 - Cadastrar Despesa\n3 - Listar Movimentações\n4 - Mostrar Saldo\n5 - Excluir Movimentação\n6 - Sair')

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
            excluir_movimentacao()
        case 6:
            print(f'Encerrando o programa :)')
            break
        case _:
            print('Opção inválida. Tente novamente\n')
