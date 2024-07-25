# A função reduce() é usada para aplicar uma função cumulativa a uma sequência de elementos, reduzindo-os a um único valor.

from functools import reduce

# Calculando a soma de uma lista de números
numeros = [1, 2, 3, 4, 5]

# Função lambda para somar dois números
soma = reduce(lambda x, y: x + y, numeros)

# Imprimindo o resultado
print(soma)  # Output: 15

# Concatenando uma lista de strings em uma única string
palavras = ["Python", "é", "incrível"]

# Função lambda para concatenar duas strings com um espaço
frase = reduce(lambda x, y: x + " " + y, palavras)

# Imprimindo o resultado
print(frase)  # Output: "Python é incrível"