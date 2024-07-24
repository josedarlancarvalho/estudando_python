"""
Resumo sobre Dictionary Comprehensions em Python

Dictionary comprehensions são uma forma concisa e eficiente de criar dicionários em Python.
Eles permitem a construção de dicionários de forma semelhante às list comprehensions,
usando uma sintaxe compacta e clara. Isso pode ser útil para transformar, filtrar e
manipular dados rapidamente.

A sintaxe básica de um dictionary comprehension é:
{chave: valor for item in iterável if condição}

Abaixo estão exemplos e explicações para ilustrar como utilizá-los.
"""

# Exemplo Básico
# Criando um dicionário onde as chaves são números de 1 a 5 e os valores são seus quadrados.
quadrados = {x: x**2 for x in range(1, 6)}
print(quadrados)  # Saída: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtragem
# Criando um dicionário que inclui apenas números pares e seus quadrados.
pares_quadrados = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(pares_quadrados)  # Saída: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transformando Dados
# Invertendo as chaves e valores de um dicionário existente.
original = {'a': 1, 'b': 2, 'c': 3}
invertido = {v: k for k, v in original.items()}
print(invertido)  # Saída: {1: 'a', 2: 'b', 3: 'c'}

# Usando Funções em Dictionary Comprehensions
# Criando um dicionário com números e seus fatores.
def fatores(n):
    return [i for i in range(1, n+1) if n % i == 0]

fatores_dict = {x: fatores(x) for x in range(1, 11)}
print(fatores_dict)  
# Saída: 
# {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5], 
#  6: [1, 2, 3, 6], 7: [1, 7], 8: [1, 2, 4, 8], 9: [1, 3, 9], 10: [1, 2, 5, 10]}

# Exemplos de Uso

# 1. Contagem de Caracteres:
# Criando um dicionário que conta a ocorrência de cada caractere em uma string.
frase = "comprehensions são úteis"
contagem = {char: frase.count(char) for char in frase}
print(contagem)  
# Saída: {'c': 1, 'o': 2, 'm': 1, 'p': 1, 'r': 1, 'e': 3, 'h': 1, 'n': 2, 's': 3, ' ': 2, 'ã': 1, 'u': 1, 't': 1, 'i': 1}

# 2. Convertendo Listas em Dicionários:
# Convertendo duas listas em um dicionário.
chaves = ['nome', 'idade', 'cidade']
valores = ['Alice', 30, 'São Paulo']
dicionario = {chaves[i]: valores[i] for i in range(len(chaves))}
print(dicionario)  # Saída: {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}

"""
Com esses exemplos e explicações, você terá uma boa base para entender e trabalhar com dictionary comprehensions em Python.
Eles são uma ferramenta poderosa para criar e manipular dicionários de maneira eficiente e elegante.
"""
