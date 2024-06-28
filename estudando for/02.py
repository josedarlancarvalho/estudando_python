'''Exercício 2: Soma de Números Ímpares
Escreva um programa que calcula a soma de todos os números ímpares em um intervalo fornecido pelo usuário.

Instruções:

Peça ao usuário para inserir os valores de início e fim do intervalo.
Use um loop for para iterar por todos os números no intervalo.
Verifique se cada número é ímpar.
Some todos os números ímpares e imprima o resultado.'''

inicio = int(input("digite o numero: "))
fim = int(input("digite outro numero: "))
soma= 0
for n in range (inicio, fim +1):
    if n % 2 == 1:
        print(f"{n} impar")
        soma += n
    else:
        print(f"{n} par")
print(f"a soma dos numeros impares é {soma}")
        