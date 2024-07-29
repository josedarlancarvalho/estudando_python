import uuid

contatos = []

def adicionar_contato():
    dict_temp = {}
    dict_temp['id'] = str(uuid.uuid4())
    dict_temp['nome'] = input("Qual nome do novo contato? ")
    dict_temp['email'] = input("Qual email do novo contato? ")
    dict_temp['telefone'] = input("Qual telefone do novo contato? ")
    contatos.append(dict_temp)
    print("Contato adicionado com sucesso.")

def excluir_contato():
    for c in contatos:
        print(f"Nome: {c['nome']}\n")
    exc = input("Qual o nome do contato que voce deseja excluir? ")
    for c in contatos:
        if exc == c['nome']:
            contatos.remove(c)
            print("Contato removido com sucesso.")
            break
    else:
        print("Nao temos ninguem com esse nome.")

def listar_contatos():
    for c in contatos:
        print(f"Nome: {c['nome']} \nEmail: {c['email']} \nTelefone: {c['telefone']}\n")
    
def buscar_contato():
    bus = input("Qual contato deseja buscar? ")
    buscar = list(filter(lambda x: x['nome'] == bus, contatos))
    if buscar:
        for c in buscar:
            print(f"Nome: {c['nome']} \nTelefone: {c['telefone']} \nEmail: {c['email']}\n")
    else:
        print("Contato nao encontrado.")
    
def maior_menor_nome():
    if contatos:
        maior = max(contatos, key=lambda x: x['nome'])
        menor = min(contatos, key=lambda x: x['nome'])
        print(f"Maior nome: {maior['nome']}")
        print(f"Menor nome: {menor['nome']}")
    else:
        print("A lista de contatos está vazia.")

def menu():
    while True:
        print('''
            ESCOLHA UMA OPÇaO
        1- ADICIONAR CONTATO
        2- REMOVER UM CONTATO
        3- LISTAR OS CONTATOS
        4- BUSCAR UM CONTATO
        5- CONTATO COM MAIOR E MENOR NOME
        6- SAIR
            ''')
        opcao = input("Qual sua opcao? ").strip()
        if opcao not in '123456' or len(opcao) != 1:
            print("Opcao invalida. Tente novamente.")
        else:
            opcao = int(opcao)
            if opcao == 1:
                adicionar_contato()
            elif opcao == 2:
                excluir_contato()
            elif opcao == 3:
                listar_contatos()
            elif opcao == 4:
                buscar_contato()
            elif opcao == 5:
                maior_menor_nome()
            elif opcao == 6:
                break

