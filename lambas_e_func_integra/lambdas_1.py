'''Exercício 1: Filtragem de Números
Crie uma lista de números inteiros de 1 a 20. Use a função filter()
junto com uma expressão lambda para obter uma nova lista contendo apenas os números divisíveis por 3.'''

inteiros = list(range(1,21))
div_3 = list(filter(lambda x: x %3 == 0, inteiros))
print(div_3)
