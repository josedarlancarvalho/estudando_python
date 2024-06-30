'''Exercício 1: Números Pares e Ímpares
Escreva um programa que solicita ao usuário um número inteiro positivo n e imprime todos os números de 1 até n, indicando se cada número é par ou ímpar.

Instruções:

Peça ao usuário para inserir um número inteiro positivo n.
Use um loop for para iterar de 1 até n.
Para cada número, verifique se ele é par ou ímpar.
Imprima o número seguido de "é par" ou "é ímpar".'''
num = int(input("digite um numero: "))
if num % 2 == 0:
    print(f"{num} é par.")
else:
    print(f"{num} é impar  ")
for n in range(1, num+ 1):
    if n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f"{n} é impar")