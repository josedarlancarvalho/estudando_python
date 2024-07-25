# Resumo sobre a função filter() em Python

# A função filter() é uma função embutida em Python que permite filtrar elementos de um iterável (como uma lista, tupla, etc.) com base em uma função que retorna True ou False. Apenas os elementos para os quais a função retorna True são incluídos no resultado.

# Sintaxe:
# filter(function, iterável)

# Parâmetros:
# - function: Uma função que testa cada elemento do iterável. Deve retornar True ou False.
# - iterável: Um iterável (como lista, tupla, etc.) cujos elementos serão filtrados.

# Exemplo básico:
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Output: [2, 4, 6]

# No exemplo acima, a função lambda x: x % 2 == 0 é aplicada a cada item da lista numeros, retornando apenas os números pares.

# Usando filter() com funções definidas pelo usuário:
def is_impar(x):
    return x % 2 != 0

impares = filter(is_impar, numeros)
print(list(impares))  # Output: [1, 3, 5]

# Importante:
# O objeto retornado pelo filter() é um iterador, o que significa que você deve convertê-lo para uma lista ou outro iterável para visualizar os resultados ou usá-lo diretamente em loops e compreensões.

# Exemplo prático com strings:
palavras = ["python", "filter", "function", "example"]
palavras_curta = filter(lambda x: len(x) < 7, palavras)
print(list(palavras_curta))  # Output: ['python', 'filter']

# Referências adicionais:
# - Documentação oficial do Python: https://docs.python.org/3/library/functions.html#filter