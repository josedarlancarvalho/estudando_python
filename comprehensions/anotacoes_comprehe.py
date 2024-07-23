# Resumo sobre List Comprehensions

"""
List Comprehensions são uma maneira concisa e eficiente de criar listas em Python. Elas permitem
a criação de novas listas a partir de sequências existentes, aplicando operações ou filtros de
maneira elegante e legível. 

Sintaxe Básica:
[expressão for item in iterável if condição]

A expressão é o valor ou operação a ser aplicada a cada item da sequência (iterável). A cláusula 
opcional 'if' é um filtro que determina quais itens serão incluídos na nova lista.

Vantagens:
- Mais conciso e legível em comparação com loops tradicionais.
- Potencialmente mais eficiente em termos de desempenho.

Exemplos:
"""

# Exemplo 1: Criar uma lista de números ao quadrado
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

# Exemplo 2: Criar uma lista de números pares
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8]

# Exemplo 3: Aplicar uma função a cada elemento de uma lista
def triplo(x):
    return x * 3

numeros = [1, 2, 3, 4, 5]
triplos = [triplo(x) for x in numeros]
print(triplos)  # Saída: [3, 6, 9, 12, 15]

# Exemplo 4: Combinar elementos de duas listas
cores = ['vermelho', 'azul', 'verde']
objetos = ['carro', 'caneta', 'bola']
combinacoes = [(c, o) for c in cores for o in objetos]
print(combinacoes)
# Saída: [('vermelho', 'carro'), ('vermelho', 'caneta'), ('vermelho', 'bola'), ...]

# Exemplo 5: Filtrar e transformar simultaneamente
palavras = ["maçã", "banana", "cereja", "damasco"]
iniciais = [palavra[0].upper() for palavra in palavras if len(palavra) > 5]
print(iniciais)  # Saída: ['B', 'D']

# List Comprehensions Aninhadas:
# É possível criar list comprehensions aninhadas, útil para trabalhar com listas de listas.

# Exemplo 6: Flattening uma lista de listas
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublista in lista_de_listas for item in sublista]
print(flattened)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Conclusão:
# List comprehensions são uma poderosa ferramenta em Python que pode simplificar o código
# e melhorar a legibilidade ao criar e manipular listas. Sua utilização adequada pode
# trazer benefícios significativos em termos de clareza e performance.

