# Resumo sobre a função reduce() em Python

# A função reduce() está disponível no módulo functools e é usada para aplicar uma função cumulativa a uma sequência de elementos, reduzindo-a a um único valor. A função cumulativa deve aceitar dois argumentos.

# Sintaxe:
# functools.reduce(function, iterável[, initial])

# Parâmetros:
# - function: Uma função que aceita dois argumentos e retorna um único valor.
# - iterável: Um iterável (como lista, tupla, etc.) cujos elementos serão reduzidos.
# - initial (opcional): Um valor inicial que é adicionado à sequência.

# Exemplo básico:
from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Output: 15

# No exemplo acima, a função lambda x, y: x + y é aplicada cumulativamente aos elementos da lista numeros, somando-os todos para produzir um único valor.

# Usando reduce() com funções definidas pelo usuário:
def multiplicar(x, y):
    return x * y

produto = reduce(multiplicar, numeros)
print(produto)  # Output: 120

# Importante:
# A função reduce() é útil para operações acumulativas onde você precisa processar todos os elementos de um iterável para obter um único valor.

# Exemplo prático com strings:
palavras = ["Python", "é", "incrível"]
frase = reduce(lambda x, y: x + " " + y, palavras)
print(frase)  # Output: "Python é incrível"

# Referências adicionais:
# - Documentação oficial do Python: https://docs.python.org/3/library/functools.html#functools.reduce
# - Tutorial sobre reduce() em Python: https://www.programiz.com/python-programming/methods/built-in/reduce