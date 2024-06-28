'''Exercício 1: Contagem de Números Pares
Escreva um programa que conta quantos números pares existem em um intervalo fornecido pelo usuário.

Instruções:

Peça ao usuário para inserir os valores de início e fim do intervalo.
Use um loop for para iterar por todos os números no intervalo.
Verifique se cada número é par.
Conte quantos números pares existem e imprima o resultado.'''

inicio = int(input("digite o numero: "))
fim = int(input("digite outro numero: "))
cont= 0

for n in range(inicio,fim +1):
    if n % 2 == 0:
        cont += 1
        print(f"{n} PAR")
        
    else:
        print("impar")

print(f"Total de números pares no intervalo: {cont}")
        
    