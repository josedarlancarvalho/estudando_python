'''
map -> aplica uma funcao para cada item de uma lista de itens

precos = [1000, 1200, 1245, 1251]

def imposto(preco)
    return preco * 1.1

LEMBRANDO, A FUNCAO TEM QUE RECEBER UM ITEM DENTRO DO () PARA O MAP FUNCIONAR

precos_impostos = []

precos_impostos = map(imposto, precos)
#saida -> <map object at 0x00000139C2639BA0>
por padrao o map nao retorna nada, apenas o map object
se quiser a saida como uma lista, é so colocar o map dentro de um list

precos_impostos = list(map(imposto, precos))
#saida -> [1100.0, 1320.0, 1369.5, 1376.1000000000001]

'''







# Resumo sobre a função map() em Python

# A função map() é uma função embutida em Python que aplica uma função a todos os itens de um iterável (como uma lista ou tupla) e retorna um map object (um iterador).

# Sintaxe:
# map(function, iterável)

# Parâmetros:
# - function: Uma função que será aplicada a cada item do iterável.
# - iterável: Um iterável (como lista, tupla, etc.) cujos itens a função será aplicada.

# Exemplo básico:
numeros = [1, 2, 3, 4, 5]
dobro = map(lambda x: x * 2, numeros)
print(list(dobro))  # Output: [2, 4, 6, 8, 10]

# No exemplo acima, a função lambda x: x * 2 é aplicada a cada item da lista numeros, resultando em uma nova lista onde cada número é multiplicado por 2.

# Usando map() com funções definidas pelo usuário:
def quadrado(x):
    return x ** 2

resultado = map(quadrado, numeros)
print(list(resultado))  # Output: [1, 4, 9, 16, 25]

# O map() pode ser usado com múltiplos iteráveis (listas, tuplas, etc.):
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
soma = map(lambda x, y: x + y, numeros1, numeros2)
print(list(soma))  # Output: [5, 7, 9]

# Vantagens do map():
# - map() é eficiente e pode ser mais rápido que loops for em alguns casos.
# - Produz um iterador que pode ser convertido em uma lista ou outros tipos de coleção.
# - Facilita a aplicação de uma função a uma coleção de itens de forma concisa e legível.

# Exemplo prático com strings:
palavras = ["python", "map", "function"]
maiusculas = map(lambda x: x.upper(), palavras)
print(list(maiusculas))  # Output: ['PYTHON', 'MAP', 'FUNCTION']

# Importante:
# O objeto retornado pelo map() é um iterador, o que significa que você deve convertê-lo para uma lista ou outro iterável para visualizar os resultados ou usá-lo diretamente em loops e compreensões.

# Referências adicionais:
# - Documentação oficial do Python: https://docs.python.org/3/library/functions.html#map
# - Tutorial sobre map() em Python: https://www.programiz.com/python-programming/methods/built-in/map


