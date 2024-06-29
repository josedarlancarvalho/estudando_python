'''Exercício 1: Quadrados dos Números
Escreva um programa que imprime o quadrado dos números de 1 a 10.

Instruções:

Use um loop for para iterar de 1 a 10.
Calcule o quadrado de cada número.
Imprima o número e seu quadrado.'''
for c in range (1, 10+1):
    a = c ** 2
    print(f"{c} - {a}")