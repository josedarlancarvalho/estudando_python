estoque = []
def adicionar_produto():
    dicio={}
    dicio ['codigo'] = input("Digite o codigo do produto: ")
    dicio ['nome'] = input("Qual o nome do produto? ")
    dicio ['preco'] = input("Qual o valor do produto? ")
    dicio ['estoque'] = input("quantos desse item tem em estoque?")
    estoque.append(dicio)
    print(estoque)

def remover_produto():
    print(estoque)
    cod = input("qual o codigo do produto que deseja remover? ")
    for i in estoque:
        if i['codigo'] == cod:
            estoque.remove(i)
            print('produto deletado.')
            break
        else:
            print("produto nao encontrado")

def atualizar_produto():
    print(estoque)
    att = input("qual produto deseja atualizar? digite o codigo do produto.")
    for i in estoque:
        if i["codigo"] == att:
            i["nome"] = input("digite o novo nome do produto: ")
            i["preco"] = input("digite o novo valor do produto: ")
            i["estoque"] = input("digite a nova quantidade do produto: ")
            print("produto atualizado.")
            break
    else:
        print("nao tem no estoque esse produto. ")
            
def listar_produtos():
    if len(estoque) == 0:
        print("Nao temos nenhum produto em estoque.")
    else:
        for c in estoque:
            print(f"codigo: {c['codigo']}, nome: {c['nome']}, preco: {c['preco']}, estoque: {c['estoque']}")

def buscar_produto():
    busca = input("digite o nome do produto que deseja buscar: ")
    for i in estoque:
        if i['nome'] == busca:
            print(f"{i['nome']} tem {i['estoque']} em estoque. ")
        else:
            print("nao tem em estoque.")
        
def menu():
    while True:
        print("""
              ESCOLHA UMA OPCAO:
              1- Adicionar produto
              2- Remover produto
              3- Atualizar produto
              4- Listar os produtos
              5- Buscar um produto
              6- SAIR
            """)
        opcao = int(input("Escolha uma opcao: "))
        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            remover_produto()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 4:
            listar_produtos()
        elif opcao == 5:
            buscar_produto()
        elif opcao == 6:
            break
        else:
            print("opcao invalida:")
            
              
    
