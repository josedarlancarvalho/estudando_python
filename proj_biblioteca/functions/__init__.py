import uuid

livros = []

def adicionar_livros():
    dict_livros = {}
    dict_livros['codigo'] = str(uuid.uuid4())
    dict_livros['titulo'] = input("Digite o titulo do livro: ")
    dict_livros['autor'] = input("Qual o autor do livro? ")
    dict_livros['publicado'] = input("Em que ano esses livro foi publicado? ")
    while True:
        disponibilidade = input("Esse livro está disponível para? [S/N]").strip().upper()
        if disponibilidade in ['S', 'N']:
            dict_livros['disponibilidade'] = disponibilidade
            break
        else:
            print("Por favor, insira 'S' para Sim ou 'N' para Não.")
    livros.append(dict_livros)
    print("livro adicionado com sucesso.")

def remover_livros():
    for c in livros:
        print(f"Codigo do livro: {c['codigo']} Titulo do livro: {c['titulo']} ")
    rem = input("Qual o titulo do livro que deseja remover? ")
    for a in livros:
        if rem in a['titulo']:
            livros.remove(a)
            print("livro removido")
            break
        else:
            print('livro nao encontrado')
        
def listar_livros():
    if not livros:
        print("Nao temos livros.")
    else:
        for c in livros:
            print(f"\nCodigo do livro: {c['codigo']} \nTitulo do livro: {c['titulo']} \nAutor: {c['autor']} \nAno de publicacao: {c['publicado']} \nDisponivel: {c['disponibilidade']}")

def buscar_livro():
    bus = input("Qual o titulo do livro que deseja buscar? ")
    for a in livros:
        if bus in a['titulo']:
            print("Temos esse livro disponivel!")
            break
        else:
            print("Nao temos esse livro disponivel!")

def emprestar_livro():
    listar_livros()
    emp = input("Qual o título do livro que você deseja? ")
    livro_encontrado = False
    for a in livros:
        if emp == a['titulo']:
            if a['disponibilidade'] == 'S':
                a['disponibilidade'] = 'N'
                print(f"Voce emprestou o livro '{a['titulo']}'.")
            else:
                print("Desculpe, este livro nao esta disponivel para emprestimo.")
            livro_encontrado = True
            break
    if not livro_encontrado:
        print("Titulo nao encontrado. Tente novamente.")

def menu():
    while True:
        print('''
            Escolha uma opção:
            1- Adicionar livro
            2- Remover livro
            3- Listar os livros
            4- Buscar livro
            5- Emprestar livro
            6- SAIR
        ''')
        opcao = int(input("Digite a opção: "))
        if opcao == 1:
            adicionar_livros()
        elif opcao == 2:
            remover_livros()
        elif opcao == 3:
            listar_livros()
        elif opcao == 4:
            buscar_livro()
        elif opcao == 5:
            emprestar_livro()
        elif opcao == 6:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
