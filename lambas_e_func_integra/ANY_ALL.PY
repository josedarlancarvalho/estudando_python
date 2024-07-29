# Resumo sobre as funções any e all em Python

# Função any
# A função any retorna True se pelo menos um dos elementos do iterável for avaliado como True.
# Caso contrário, retorna False.
# É equivalente a um operador "OU" lógico aplicado a uma coleção de valores.

# Exemplo 1: Usando a função any
valores1 = [0, 0, 1, 0]
resultado_any1 = any(valores1)
print(f"Resultado de any(valores1): {resultado_any1}")  # Saída: True

# Exemplo 2: Usando a função any com todos os valores False
valores2 = [0, 0, 0, 0]
resultado_any2 = any(valores2)
print(f"Resultado de any(valores2): {resultado_any2}")  # Saída: False

# Função all
# A função all retorna True se todos os elementos do iterável forem avaliados como True.
# Caso contrário, retorna False.
# É equivalente a um operador "E" lógico aplicado a uma coleção de valores.

# Exemplo 1: Usando a função all
valores3 = [1, 1, 1, 1]
resultado_all1 = all(valores3)
print(f"Resultado de all(valores3): {resultado_all1}")  # Saída: True

# Exemplo 2: Usando a função all com um valor False
valores4 = [1, 1, 0, 1]
resultado_all2 = all(valores4)
print(f"Resultado de all(valores4): {resultado_all2}")  # Saída: False

# Uso em combinações mais complexas
# Verificando se há pelo menos um número par na lista
numeros = [1, 3, 5, 8]
tem_par = any(num % 2 == 0 for num in numeros)
print(f"Tem pelo menos um número par em numeros: {tem_par}")  # Saída: True

# Verificando se todos os números são ímpares na lista
todos_impares = all(num % 2 != 0 for num in numeros)
print(f"Todos os números são ímpares em numeros: {todos_impares}")  # Saída: False
