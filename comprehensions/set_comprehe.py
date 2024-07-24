"""
Resumo sobre Set Comprehensions em Python

Set comprehensions são uma forma concisa e eficiente de criar conjuntos (sets) em Python.
Eles permitem a construção de sets de forma semelhante às list comprehensions, usando uma sintaxe compacta e clara.
Isso pode ser útil para criar coleções de elementos únicos, aplicar transformações e filtros rapidamente.

A sintaxe básica de um set comprehension é:
{expressão for item in iterável if condição}

Abaixo estão exemplos e explicações para ilustrar como utilizá-los.
"""

# Exemplo Básico
# Criando um conjunto de números de 1 a 5.
numeros = {x for x in range(1, 6)}
print(numeros)  # Saída: {1, 2, 3, 4, 5}

# Filtragem
# Criando um conjunto de números pares de 1 a 10.
pares = {x for x in range(1, 11) if x % 2 == 0}
print(pares)  # Saída: {2, 4, 6, 8, 10}

# Transformando Dados
# Criando um conjunto com o comprimento das palavras em uma lista.
palavras = ["Python", "é", "muito", "legal"]
comprimentos = {len(palavra) for palavra in palavras}
print(comprimentos)  # Saída: {2, 5, 6}

# Removendo Duplicatas
# Criando um conjunto a partir de uma lista com duplicatas para obter elementos únicos.
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
conjunto_unico = {x for x in lista_com_duplicatas}
print(conjunto_unico)  # Saída: {1, 2, 3, 4, 5}

# Exemplos de Uso

# 1. Filtragem de Caracteres Únicos:
# Criando um conjunto de caracteres únicos de uma string.
frase = "set comprehensions são úteis"
caracteres_unicos = {char for char in frase if char != ' '}
print(caracteres_unicos)  
# Saída: {'a', 'c', 'e', 'h', 'i', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'ã'}

# 2. Números Quadrados:
# Criando um conjunto de quadrados de números de 1 a 10.
quadrados = {x**2 for x in range(1, 11)}
print(quadrados)  # Saída: {64, 1, 4, 36, 9, 16, 49, 81, 100, 25}

# 3. Elementos Únicos de uma Lista:
# Criando um conjunto com elementos únicos de uma lista.
lista = [1, 2, 3, 1, 2, 4, 5]
unicos = {x for x in lista}
print(unicos)  # Saída: {1, 2, 3, 4, 5}

"""
Com esses exemplos e explicações, você terá uma boa base para entender e trabalhar com set comprehensions em Python.
Eles são uma ferramenta poderosa para criar e manipular conjuntos de maneira eficiente e elegante.
"""
