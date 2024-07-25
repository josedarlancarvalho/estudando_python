"""
Resumo sobre Expressões Lambda em Python

Expressões lambda são funções anônimas, ou seja, funções sem nome, que podem ser definidas em uma única linha de código.
Elas são frequentemente usadas para criar funções simples e rápidas, especialmente quando são passadas como argumentos 
para funções de ordem superior como map(), filter(), sorted() e reduce().

A sintaxe básica de uma expressão lambda é:
lambda argumentos: expressão

Abaixo estão exemplos e explicações para ilustrar como utilizá-las.
"""

# Exemplo Básico
# Criando uma função lambda para adicionar dois números.
soma = lambda a, b: a + b
print(soma(3, 5))  # Saída: 8

# Usando lambda com map()
# Aplicando uma função lambda a cada elemento de uma lista.
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

# Usando lambda com filter()
# Filtrando uma lista para obter apenas números pares.
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6]

# Usando lambda com sorted()
# Ordenando uma lista de tuplas pelo segundo elemento.
tuplas = [(1, 'um'), (2, 'dois'), (3, 'três')]
ordenado = sorted(tuplas, key=lambda x: x[1])
print(ordenado)  # Saída: [(2, 'dois'), (1, 'um'), (3, 'três')]

# Usando lambda com reduce()
# Calculando o produto de todos os elementos de uma lista.
from functools import reduce
numeros = [1, 2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, numeros)
print(produto)  # Saída: 120

# Lambda em Funções de Ordem Superior
# Funções que retornam funções lambda.
def multiplicador(n):
    return lambda x: x * n

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(5))  # Saída: 10
print(triplo(5))  # Saída: 15

# Usando lambda com listas aninhadas
# Ordenando uma lista de dicionários pelo valor de uma chave específica.
pessoas = [{'nome': 'João', 'idade': 25}, {'nome': 'Maria', 'idade': 30}, {'nome': 'Pedro', 'idade': 20}]
ordenado_por_idade = sorted(pessoas, key=lambda pessoa: pessoa['idade'])
print(ordenado_por_idade)
# Saída: [{'nome': 'Pedro', 'idade': 20}, {'nome': 'João', 'idade': 25}, {'nome': 'Maria', 'idade': 30}]

"""
Com esses exemplos e explicações, você terá uma boa base para entender e trabalhar com expressões lambda em Python.
Elas são uma ferramenta poderosa para criar funções rápidas e eficientes de maneira concisa.
"""
