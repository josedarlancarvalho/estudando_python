# resumo_funcoes_integradas.py

"""
Resumo sobre as funções integradas len, abs, sum e round em Python.
"""

# Função len()
# A função len() retorna o número de itens em um objeto. O objeto pode ser uma sequência (como uma string, lista ou tupla) ou um contêiner (como um dicionário ou conjunto).
exemplo_lista = [1, 2, 3, 4, 5]
tamanho_lista = len(exemplo_lista)  # Retorna 5
print(f"Tamanho da lista: {tamanho_lista}")

# Função abs()
# A função abs() retorna o valor absoluto de um número. O valor absoluto é a distância do número até zero, sem considerar a direção (positivo ou negativo).
numero_negativo = -7
valor_absoluto = abs(numero_negativo)  # Retorna 7
print(f"Valor absoluto de {numero_negativo}: {valor_absoluto}")

# Função sum()
# A função sum() retorna a soma dos números em um iterável. Pode-se também passar um segundo argumento que será somado ao resultado final.
numeros = [1, 2, 3, 4, 5]
soma_numeros = sum(numeros)  # Retorna 15
print(f"Soma dos números: {soma_numeros}")

# Função round()
# A função round() retorna um número arredondado para um número específico de dígitos após o ponto decimal. Se nenhum número de dígitos for fornecido, arredonda para o inteiro mais próximo.
numero_decimal = 3.14159
numero_arredondado = round(numero_decimal, 2)  # Retorna 3.14
print(f"Numero {numero_decimal} arredondado para 2 casas decimais: {numero_arredondado}")

# Exemplos adicionais

# len() com string
exemplo_string = "Python"
tamanho_string = len(exemplo_string)  # Retorna 6
print(f"Tamanho da string: {tamanho_string}")

# abs() com número positivo
numero_positivo = 5
valor_absoluto_positivo = abs(numero_positivo)  # Retorna 5
print(f"Valor absoluto de {numero_positivo}: {valor_absoluto_positivo}")

# sum() com valor inicial
soma_com_inicial = sum(numeros, 10)  # Retorna 25
print(f"Soma dos números com valor inicial 10: {soma_com_inicial}")

# round() sem especificar casas decimais
numero_arredondado_sem_casas = round(numero_decimal)  # Retorna 3
print(f"Numero {numero_decimal} arredondado: {numero_arredondado_sem_casas}")
