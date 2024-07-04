'''Exercício 7: Média de Números
Escreva um programa que solicita ao usuário 5 números e calcula a média desses números.
Instruções:
Use um loop for para solicitar ao usuário 5 números.
Some os números.
Calcule a média.
Imprima a média.'''
soma = 0
for n in range (0,5) :
    n += 1
    num = int(input("digite um numero: "))
    soma += num
total = soma / 5
print(total)