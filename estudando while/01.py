'''
Exercício: Somar números até o usuário digitar zero
Escreva um programa que peça ao usuário para digitar números inteiros e some esses números.
O programa deve continuar pedindo números até que o usuário digite 0. 
Quando 0 for digitado, o programa deve exibir a soma de todos os números digitados (excluindo o 0).
'''
n = int(input("digite um numero: "))
soma = n
while n != 0:
    n = int(input("digite um numero: "))
    if n == 0:
        break
    soma += n
print(f"soma dos numeros: {soma}")