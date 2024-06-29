'''Exercício 2: Tabuada
Escreva um programa que imprime a tabuada de um número fornecido pelo usuário.

Instruções:

Peça ao usuário para inserir um número.
Use um loop for para iterar de 1 a 10.
Calcule e imprima a multiplicação do número inserido pelo usuário com cada número de 1 a 10.'''
n = int(input("digite um numero:"))
for c in range(1, 10 + 1):
    mult = n * c
    print(f"{n} x {c} = {mult}")