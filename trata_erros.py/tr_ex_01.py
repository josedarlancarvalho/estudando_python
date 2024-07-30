'''Crie uma pequena calculadora que solicita ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão). 
Use try e except para tratar possíveis erros, como divisão por zero e entrada de valores não numéricos. Passos:
Solicite ao usuário dois números.
Solicite ao usuário a operação desejada (adição, subtração, multiplicação ou divisão).
Execute a operação desejada e exiba o resultado.
Use try e except para tratar:
Divisão por zero.
Entrada de valores não numéricos.'''
def calculadora():
    try:
        num_1 = float(input("Digite o primeiro numero: "))
        num_2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("por favor, digite valores numericos validos.")
        return

    while True:
        print('''
        ESCOLHA UMA OPERAÇÃO:
        1- ADIÇÃO
        2- SUBTRAÇÃO
        3- MULTIPLICAÇÃO
        4- DIVISAO
        0- SAIR
        ''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um numero valido para a operaçao.")
            continue
        
        if opcao == 1:
            soma = num_1 + num_2
            print(f"{num_1} + {num_2} = {soma}")
        elif opcao == 2:
            subtracao = num_1 - num_2
            print(f"{num_1} - {num_2} = {subtracao}")
        elif opcao == 3:
            multiplicacao = num_1 * num_2
            print(f"{num_1} * {num_2} = {multiplicacao}")
        elif opcao == 4:
            try:
                divisao = num_1 / num_2
                print(f"{num_1} / {num_2} = {divisao}")
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

calculadora()
