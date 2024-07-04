'''Tabuada
Escreva um programa que gere a tabuada de um número fornecido pelo usuário. A tabuada deve ser gerada de 1 a 10.'''
num = int(input("Digite um numero: "))
for c in range (1, 11):
    tabuada = num * c
    print(f"{num} x {c} = {tabuada}")