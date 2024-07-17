'''Exercício 4: Escreva uma função chamada contar_vogais que recebe 
uma string como parâmetro e retorna a quantidade de vogais presentes na string.'''
def contar_vogais(palavra):
    vogais = 'aeiouAEIOU'
    cont = 0
    for c in palavra: 
        if c in vogais:
            cont += 1
    return cont
a = contar_vogais("darlan")
print(a)
