'''Exercício 4: Números Primos
Escreva um programa que solicita ao usuário um número inteiro positivo n e imprime todos os números primos de 1 até n.

Instruções:

Peça ao usuário para inserir um número inteiro positivo n.
Use um loop for para iterar de 2 até n.
Para cada número, verifique se ele é primo.
Imprima os números primos.'''
numero_usuario = int(input("digite um numero:"))

for num in range (2, numero_usuario +1):
    primo = True
    for i in range (2 , int(num*0.5) + 1):
        if num % i == 0:
            primo = False
    if primo:
        print(num)