'''Atividades com for Soma de Números Pares
Escreva um programa que some todos os números pares de 1 a 100 e imprima o resultado.'''
soma = 0
for c in range (1, 101):
    if c % 2 == 0:
        soma += c
print(soma)