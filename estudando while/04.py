'''Adivinhação de Número
Escreva um programa que escolha um número aleatório entre 1 e 100. Peça ao usuário para adivinhar o número
e forneça feedback se o palpite estiver muito alto, muito baixo ou correto.
O loop deve continuar até que o usuário adivinhe o número corretamente.'''
import random
pc = random.randint(1,100)
while True:
    n = int(input("digite um numero: [1-100]"))
    if n == pc:
        print(f"acertou! foi o numero {n}")
        break
    if n > pc:
        print("menor")
    elif n < pc:
        print("maior")
