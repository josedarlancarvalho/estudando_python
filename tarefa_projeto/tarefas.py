lista_tarefas = []

def adicionar_tarefa():
    tarefa = {}
    tarefa['titulo'] = input("Qual título da tarefa que deseja adicionar? ")
    tarefa['descricao'] = input("Qual descrição da tarefa deseja adicionar? ")
    tarefa['status'] = False
    lista_tarefas.append(tarefa)

def remover_tarefa():
    titulo = input("Qual o título da tarefa que deseja excluir? ")
    for tarefa in lista_tarefas:
        if tarefa['titulo'] == titulo:
            lista_tarefas.remove(tarefa)
            print(f"Tarefa '{titulo}' removida com sucesso.")
            return
    print("Título inválido. Tente novamente.")


def listar_tarefas():
    if not lista_tarefas:
        print("Nenhuma tarefa adicionada.")
    for tarefa in lista_tarefas:
        status = "Concluída" if tarefa['status'] else "Pendente"
        print(f"Título: {tarefa['titulo']}, Descrição: {tarefa['descricao']}, Status: {status}")

def concluir_tarefa():
    titulo = input("Qual tarefa deseja marcar como concluída? Digite o título: ")
    for tarefa in lista_tarefas:
        if tarefa['titulo'] == titulo:
            tarefa['status'] = True
            print(f"Tarefa '{titulo}' marcada como concluída.")
            return
    print("Título inválido. Tente novamente.")

def gerenciar_tarefas():
    while True:
        print("""
Selecione uma opção:
1 = Adicionar tarefa
2 = Remover tarefa
3 = Listar as tarefas
4 = Concluir uma tarefa
5 = Sair
        """)
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            remover_tarefa()
        elif opcao == 3:
            listar_tarefas()
        elif opcao == 4:
            concluir_tarefa()
        elif opcao == 5:
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

gerenciar_tarefas()