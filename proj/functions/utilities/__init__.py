agenda = []

def adicionar_compromisso():
    dicio = {}
    dicio ['titulo'] = input("qual o titulo do compromisso? ")
    dicio ['data'] = input("qual a data do compromisso? [DD-MM-AAAA] ")
    dicio ['hora'] = input("qual o horario do compromisso? [HH:MM] ")
    agenda.append(dicio)

def remover_compromisso():
    for i, compromisso in enumerate(agenda):
       print(f"{i+1}- {compromisso['titulo']} - {compromisso['data']} as {compromisso['hora']}")
    deletar = str(input("digite o titulo do compromisso que deseja deletar: "))
    for compromisso in agenda:
        if compromisso['titulo'] == deletar:
            agenda.remove(compromisso)
            print("compromisso deletado. ")
            break
        else:
            print("nao encontramos esse compromisso.")

def listar_compromisso():
    if not agenda:
        print("Não há compromissos.")
    for compromisso in agenda:
        print(f"Título: {compromisso['titulo']}, Data: {compromisso['data']}, Hora: {compromisso['hora']}")

def iniciar_programa():
    while True:
        print("""
            ESCOLHA UMA OPÇÃO:
            1- ADICIONAR COMPROMISSO
            2- REMOVER COMPROMISSO
            3- LISTAR COMPROMISSOS
            4- SAIR
        """)
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionar_compromisso()
        elif opcao == 2:
            remover_compromisso()
        elif opcao == 3:
            listar_compromisso()
        elif opcao == 4:
            break
        else:
            print("opção invalida.")

            