'''Exercício 3: Impressão de Nomes
Escreva um programa que pede ao usuário para inserir cinco nomes e, em seguida, imprime cada nome com uma mensagem de saudação.

Instruções:

Use um loop for para pedir ao usuário que insira cinco nomes.
Use outro loop for para iterar sobre os nomes inseridos.
Imprima uma mensagem de saudação para cada nome.'''
nomes = []
for n in range(5):
    nome = input("Insira um nome: ")
    nomes.append(nome)  

for nome in nomes:
    print(f"Saudação: {nome}")
