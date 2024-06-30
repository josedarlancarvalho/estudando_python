'''Exercício 3: Número de Dígitos
Escreva um programa que solicita ao usuário um número inteiro e imprime o número de dígitos desse número.

Instruções:

Peça ao usuário para inserir um número inteiro.
Use um loop for para contar os dígitos do número.
Imprima o número de dígitos.'''
num = int(input("digite um numero:"))
cont = 0
for c in range (0, 1):
    if num < 10:
        print(f"{num} tem 1 digito")
    elif num > 10 and num > 100:
        print(f"{num} tem 2 digitos")
    elif num > 100 and num > 1000:
        print(f"{num} tem 3 digitos")
    elif num > 1000 and num > 10000:
        print(f"{num} tem 4 digitos")
  
    