# resumo_zip.py

"""
Resumo sobre a função zip em Python.
"""

# Função zip()
# A função zip() em Python combina elementos de múltiplos iteráveis (como listas ou tuplas) em tuplas. 
# O zip() para quando o iterável mais curto é exaurido.

# Exemplos básicos
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [True, False, True]

# Combinando duas listas
zip_result = zip(lista1, lista2)
print(f"Zip de lista1 e lista2: {list(zip_result)}")
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Combinando três listas
zip_result = zip(lista1, lista2, lista3)
print(f"Zip de lista1, lista2 e lista3: {list(zip_result)}")
# Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# Usando zip em loops
for num, char in zip(lista1, lista2):
    print(f"Número: {num}, Letra: {char}")

# Descompactando usando zip()
dados_zip = zip(lista1, lista2)
nums, chars = zip(*dados_zip)
print(f"Números descompactados: {nums}")
print(f"Letras descompactadas: {chars}")

# Usos práticos
# Criando um dicionário a partir de duas listas
chaves = ['nome', 'idade', 'cidade']
valores = ['Alice', 25, 'São Paulo']
dicionario = dict(zip(chaves, valores))
print(f"Dicionário criado a partir de duas listas: {dicionario}")

# Iterando sobre múltiplas listas simultaneamente
nomes = ['Alice', 'Bob', 'Charlie']
idades = [25, 30, 35]
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']

for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f"{nome} tem {idade} anos e mora em {cidade}.")

# Lidando com iteráveis de tamanhos diferentes
# zip() para no menor iterável
curta_lista = [1, 2]
longa_lista = ['a', 'b', 'c']

zip_result = zip(curta_lista, longa_lista)
print(f"Zip de listas de tamanhos diferentes: {list(zip_result)}")
# Output: [(1, 'a'), (2, 'b')]

# Exemplo com diferentes tipos de iteráveis
tupla = (10, 20, 30)
string = "abc"
zip_result = zip(lista1, tupla, string)
print(f"Zip de diferentes tipos de iteráveis: {list(zip_result)}")
# Output: [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]
