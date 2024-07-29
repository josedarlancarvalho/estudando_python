# sorted_summary.py

# Resumo sobre a função sorted()

"""
A função sorted() em Python é usada para retornar uma nova lista ordenada a partir dos elementos de qualquer iterável.
Ela não modifica o iterável original, ao contrário do método sort() que é usado em listas.

Sintaxe:
    sorted(iterable, key=None, reverse=False)

Parâmetros:
    - iterable: qualquer iterável (lista, tupla, dicionário, etc.) cujos elementos você deseja ordenar.
    - key (opcional): uma função que serve como chave para a comparação de elementos.
    - reverse (opcional): um valor booleano. Se True, a lista é ordenada em ordem decrescente.

Retorna:
    Uma nova lista ordenada.

Exemplos:
"""

# Exemplo 1: Ordenando uma lista de números
numeros = [5, 2, 9, 1, 5, 6]
numeros_ordenados = sorted(numeros)
print("Números ordenados:", numeros_ordenados)
# Saída: Números ordenados: [1, 2, 5, 5, 6, 9]

# Exemplo 2: Ordenando uma lista de strings
palavras = ["banana", "apple", "cherry"]
palavras_ordenadas = sorted(palavras)
print("Palavras ordenadas:", palavras_ordenadas)
# Saída: Palavras ordenadas: ['apple', 'banana', 'cherry']

# Exemplo 3: Ordenando com a chave (key) personalizada
pessoas = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Ana', 'idade': 22},
    {'nome': 'Carlos', 'idade': 30}
]
pessoas_ordenadas_por_idade = sorted(pessoas, key=lambda pessoa: pessoa['idade'])
print("Pessoas ordenadas por idade:", pessoas_ordenadas_por_idade)
# Saída: Pessoas ordenadas por idade: [{'nome': 'Ana', 'idade': 22}, {'nome': 'João', 'idade': 25}, {'nome': 'Carlos', 'idade': 30}]

# Exemplo 4: Ordenando em ordem decrescente
numeros_decrescentes = sorted(numeros, reverse=True)
print("Números em ordem decrescente:", numeros_decrescentes)
# Saída: Números em ordem decrescente: [9, 6, 5, 5, 2, 1]

# Exemplo 5: Ordenando uma lista de tuplas
tuplas = [(1, 'um'), (3, 'três'), (2, 'dois')]
tuplas_ordenadas = sorted(tuplas)
print("Tuplas ordenadas:", tuplas_ordenadas)
# Saída: Tuplas ordenadas: [(1, 'um'), (2, 'dois'), (3, 'três')]

"""
Observações:
- A função sorted() é versátil e pode ser usada com qualquer tipo de iterável.
- Quando usada com dicionários, sorted() retorna uma lista das chaves ordenadas.
- A função key é muito útil para ordenações personalizadas, como ordenar objetos complexos.

A função sorted() é uma ferramenta essencial no arsenal de um programador Python, permitindo ordenações eficientes e flexíveis.
"""

# Exemplos adicionais e testes podem ser feitos para compreender melhor o uso da função sorted().
