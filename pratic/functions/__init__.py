tarefas = []
def adicionar_tarefa():
    dici = {}
    dici ['titulo'] = input("qual o titulo da tarefa? ")
    dici ['descricao'] = input("qual a descricao da tarefa? ")	
    tarefas.append(dici)

def remover_tarefa():
    global tarefas
    exc = input("Qual o título da tarefa que deseja excluir? ")
    tarefas = list(filter(lambda t: t['titulo'] != exc, tarefas))
    if len(tarefas) == 0:   
        print("Tarefa removida! Não tem nenhuma tarefa na lista mais.")
    else:
        print("Tarefa removida! Segue as tarefas que existem:")
        for c in tarefas:
            print(f"Titulo: {c['titulo']} \nDescrição: {c['descricao']}")

def listar_tarefas():
    print('-' * 30)
    for c in tarefas:
        print(f"Titulo: {c['titulo']} \nDescrição: {c['descricao']}")
    print('-' * 30)

def buscar_tarefas():
    bus = input("digite o titulo da tarefa que deseja buscar: ")
    buscar = (list(filter(lambda a: a['titulo'] == bus, tarefas)))
    print(buscar)

def resumo_tarefas():
    res = input("Digite um trecho da descrição da tarefa que deseja buscar: ")
    resumo = list(filter(lambda a: res in a['descricao'], tarefas))
    print(resumo)

def menu():
    while True:    
        print('''
            Escolha uma opção:
            1- Adicionar tarefa
            2- Remover tarefa
            3- Listar as tarefas
            4- Buscar tarefas
            5- Resumo das tarefas 
            6- SAIR
           ''')
        a = 1,2,3,4,5,6
        opcao = int(input("digite a opcao:"))
        if opcao not in a:
            print("opcao invalida.")
        elif opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            remover_tarefa()
        elif opcao == 3:
            listar_tarefas()
        elif opcao == 4:
            buscar_tarefas()
        elif opcao == 5:
            resumo_tarefas()
        elif opcao == 6:
            break
