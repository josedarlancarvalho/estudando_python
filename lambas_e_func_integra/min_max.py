# min_max_summary.py

# Resumo sobre as funções min() e max()

"""
As funções integradas min() e max() em Python são usadas para encontrar, respectivamente, o menor e o maior valor em um iterável, ou para encontrar o menor e o maior valor entre dois ou mais argumentos.

Sintaxe:
    min(iterable, *[, key, default])
    max(iterable, *[, key, default])
    min(arg1, arg2, *args[, key])
    max(arg1, arg2, *args[, key])

Parâmetros:
    - iterable: qualquer iterável (lista, tupla, dicionário, etc.) cujos elementos você deseja comparar.
    - arg1, arg2, *args: dois ou mais argumentos para comparação direta.
    - key (opcional): uma função que serve como chave para a comparação de elementos.
    - default (opcional): o valor retornado se o iterável estiver vazio.

Retorna:
    O menor valor com min() e o maior valor com max().

Exemplos:
"""

# Exemplo 1: Encontrando o menor e o maior número em uma lista
numeros = [5, 2, 9, 1, 5, 6]
menor_numero = min(numeros)
maior_numero = max(numeros)
print("Menor número:", menor_numero)
print("Maior número:", maior_numero)
# Saída: Menor número: 1
#        Maior número: 9

# Exemplo 2: Comparando dois ou mais números diretamente
menor_valor = min(10, 20, 5, 30)
maior_valor = max(10, 20, 5, 30)
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
# Saída: Menor valor: 5
#        Maior valor: 30

# Exemplo 3: Encontrando o menor e o maior string em uma lista
palavras = ["banana", "apple", "cherry"]
menor_palavra = min(palavras)
maior_palavra = max(palavras)
print("Menor palavra:", menor_palavra)
print("Maior palavra:", maior_palavra)
# Saída: Menor palavra: apple
#        Maior palavra: cherry

# Exemplo 4: Usando a chave (key) personalizada para encontrar o menor e o maior dicionário baseado em uma chave específica
pessoas = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Ana', 'idade': 22},
    {'nome': 'Carlos', 'idade': 30}
]
menor_idade = min(pessoas, key=lambda pessoa: pessoa['idade'])
maior_idade = max(pessoas, key=lambda pessoa: pessoa['idade'])
print("Pessoa com menor idade:", menor_idade)
print("Pessoa com maior idade:", maior_idade)
# Saída: Pessoa com menor idade: {'nome': 'Ana', 'idade': 22}
#        Pessoa com maior idade: {'nome': 'Carlos', 'idade': 30}

# Exemplo 5: Usando o parâmetro default
numeros_vazios = []
menor_numero_default = min(numeros_vazios, default="Nenhum valor")
maior_numero_default = max(numeros_vazios, default="Nenhum valor")
print("Menor número com default:", menor_numero_default)
print("Maior número com default:", maior_numero_default)
# Saída: Menor número com default: Nenhum valor
#        Maior número com default: Nenhum valor

"""
Observações:
- As funções min() e max() são extremamente úteis para comparações simples e rápidas.
- Elas podem ser usadas com qualquer tipo de dados que seja comparável, incluindo números, strings, e objetos personalizados.
- O parâmetro key permite flexibilidade adicional, permitindo a ordenação baseada em atributos ou transformações dos elementos.
- O parâmetro default é útil para evitar exceções ao lidar com iteráveis vazios.

Essas funções são ferramentas fundamentais que simplificam a busca por extremos em coleções de dados.
"""

# Exemplos adicionais e testes podem ser feitos para compreender melhor o uso das funções min() e max().
