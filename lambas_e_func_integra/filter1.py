# A função filter() é usada para filtrar elementos de um iterável com base em uma condição.

# Filtrando números pares de uma lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função lambda para verificar se um número é par
pares = filter(lambda x: x % 2 == 0, numeros)

# Convertendo o resultado para uma lista e imprimindo
print(list(pares))  # Output: [2, 4, 6, 8, 10]

# Filtrando palavras com menos de 5 letras
palavras = ["python", "filter", "lambda", "code", "test"]

# Função lambda para verificar o comprimento da palavra
curtas = filter(lambda x: len(x) < 5, palavras)

# Convertendo o resultado para uma lista e imprimindo
print(list(curtas))  # Output: ['code', 'test']
