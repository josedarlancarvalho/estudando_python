'''Exercício 5: Fatorial de um Número
Escreva um programa que solicita ao usuário um número inteiro positivo n e calcula o fatorial de n.

Instruções:

Peça ao usuário para inserir um número inteiro positivo n.
Use um loop for para calcular o fatorial de n.
Utilize uma estrutura de condição para verificar e multiplicar os números.
Imprima o fatorial de n.'''
n = int(input("Digite um número inteiro positivo: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"O fatorial de {n} é {fatorial}")
