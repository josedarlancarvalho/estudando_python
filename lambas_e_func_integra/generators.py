# Resumo sobre Generators em Python

# O que são Generators?
# Generators são uma forma de criar iteradores em Python. Eles permitem que você 
# produza uma sequência de valores de maneira "preguiçosa", ou seja, os valores 
# são gerados sob demanda e não todos de uma vez, economizando memória.

# Como criar um Generator?
# Você pode criar um generator usando funções com a palavra-chave 'yield' ou 
# usando expressões generator (semelhantes a comprehensions de lista, mas com parênteses).

# Exemplo de função generator com 'yield'
def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

# Usando o generator
gen = contador(5)
for num in gen:
    print(num)
# Saída: 0 1 2 3 4

# Exemplo de expressão generator
gen_exp = (x ** 2 for x in range(5))
for num in gen_exp:
    print(num)
# Saída: 0 1 4 9 16

# Vantagens dos Generators:
# 1. Memória Eficiente: Como os valores são gerados sob demanda, você não precisa 
#    armazenar grandes listas na memória.
# 2. Padrão de Design Simples: Generators facilitam a implementação de padrões de 
#    iteração complexos.

# Usando a função next()
# Você pode usar a função next() para obter o próximo valor de um generator.
gen = contador(3)
print(next(gen))  # Saída: 0
print(next(gen))  # Saída: 1
print(next(gen))  # Saída: 2
# print(next(gen))  # Isto causaria um erro StopIteration

# Generators vs Iterators
# Todos os generators são iteradores, mas nem todos os iteradores são generators.
# Generators são uma maneira conveniente e eficiente de criar iteradores.

# Exemplo prático: Leitura de arquivos grandes
def ler_arquivo_grande(file_name):
    with open(file_name) as f:
        for linha in f:
            yield linha

# Usando o generator para ler um arquivo grande linha por linha
for linha in ler_arquivo_grande("arquivo_grande.txt"):
    print(linha)

# Conclusão:
# Generators são uma ferramenta poderosa em Python, especialmente útil para 
# trabalhar com grandes conjuntos de dados ou streams de dados, onde a eficiência 
# de memória é crucial.
