'''
Exercício 2: Soma de Múltiplos de 3 e 5

Escreva um programa que calcula a soma de todos os números múltiplos de 3 ou 5 abaixo de 1000.

Instruções:

Use um loop for para iterar de 1 a 999.
Para cada número, verifique se ele é múltiplo de 3 ou 5.
Some todos os números que são múltiplos de 3 ou 5.
Imprima a soma total.'''
cont = 0
for n in range (1, 999+1):
    if n % 3 == 0 or n % 5 == 0:
         cont += n
         if n % 3 == 0 and n % 5 == 0:
            print(f"{n} é divisivel por 3 e 5")
         elif n % 3 == 0:
             print(f"{n} é divisivel por 3")
         elif n % 5 == 0:
             print(f"{n} é divisivel por 5")
print(cont)