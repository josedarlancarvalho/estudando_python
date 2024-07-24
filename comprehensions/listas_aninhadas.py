"""
Resumo sobre Listas Aninhadas em Python

Listas aninhadas são listas que contêm outras listas como elementos. Elas são úteis para
representar estruturas de dados multidimensionais, como tabelas, matrizes ou grafos.
Com listas aninhadas, é possível organizar e acessar dados complexos de maneira eficiente.
"""

# Criação de Listas Aninhadas
# Lista aninhada representando uma matriz 2x2
matriz = [
    [1, 2],
    [3, 4]
]

# Acesso a Elementos
# Para acessar elementos em listas aninhadas, utiliza-se a notação de índices múltiplos:
print(matriz[0][1])  # Saída: 2
print(matriz[1][0])  # Saída: 3

# Iteração sobre Listas Aninhadas
# É comum iterar sobre listas aninhadas usando loops aninhados:
for linha in matriz:
    for elemento in linha:
        print(elemento)

# Modificação de Elementos
# Elementos dentro de listas aninhadas podem ser modificados da mesma forma que em listas comuns:
matriz[0][1] = 20
print(matriz)  # Saída: [[1, 20], [3, 4]]

# Exemplos de Uso

# 1. Tabela de Dados:
# Listas aninhadas são úteis para armazenar tabelas de dados, onde cada sublista representa uma linha:
tabela = [
    ["Nome", "Idade", "Cidade"],
    ["Alice", 30, "São Paulo"],
    ["Bob", 25, "Rio de Janeiro"],
    ["Charlie", 35, "Belo Horizonte"]
]

for linha in tabela:
    print(linha)

# 2. Matriz:
# Representação de uma matriz 3x3:
matriz_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Somando todos os elementos da matriz
soma = 0
for linha in matriz_3x3:
    for elemento in linha:
        soma += elemento
print(soma)  # Saída: 45

# 3. Grafo:
# Representação de um grafo utilizando listas aninhadas
grafo = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]

# Verificando a existência de uma aresta entre dois vértices
vertice1 = 0
vertice2 = 1
if grafo[vertice1][vertice2] == 1:
    print(f"Existe uma aresta entre os vértices {vertice1} e {vertice2}.")
else:
    print(f"Não existe uma aresta entre os vértices {vertice1} e {vertice2}.")

"""
Com esses exemplos e explicações, você terá uma boa base para entender e trabalhar com listas
aninhadas em Python. Elas são uma ferramenta poderosa para manipulação de dados complexos e
multidimensionais.
"""
