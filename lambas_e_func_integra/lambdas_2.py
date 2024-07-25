'''Exercício 2: Ordenação de Palavras
Crie uma lista de palavras. Use a função sorted() junto com uma expressão lambda
para ordenar as palavras em ordem crescente pelo número de caracteres que elas possuem.'''

palavras = ['fone','cabo', 'monitor', 'mouse', 'teclado']
a = sorted(palavras, key=lambda x: len(x))
print (a)