'''Exercício: Calculadora de Média de Notas
Crie um programa que tenha uma função chamada calcular_media que recebe uma lista de dicionários.
Cada dicionário representa um aluno com o nome e uma lista de notas. A função deve calcular e retornar
 a média das notas de cada aluno. Além disso, crie uma função situacao_aluno que receba a média calculada
   e retorne "Aprovado" se a média for maior ou igual a 7, e "Reprovado" caso contrário.
Requisitos:
A função calcular_media deve receber uma lista de dicionários, onde cada dicionário 
contém o nome do aluno e suas notas.
A função deve retornar uma nova lista de dicionários, onde cada dicionário contém o nome do aluno
 sua média de notas e sua situação ("Aprovado" ou "Reprovado").
A função situacao_aluno deve receber a média e retornar "Aprovado" ou "Reprovado".'''
def calcular_media(alunos):
    resultado = []
    for aluno in alunos:
        nome = aluno['nome']
        notas = aluno ['notas']
        media = sum(notas) / len(notas)
        situacao = situacao_aluno(media)
        resultado.append({'nome': nome, 'media' : round(media, 2), 'situacao': situacao})
        return resultado
def situacao_aluno(media):
    if media >= 7:
        return ('aprovado')
    else:
        return("reprovado")

alunos = [
    {"nome": "Alice", "notas": [8, 7.5, 9]},
    {"nome": "Bob", "notas": [6, 5.5, 7]},
    {"nome": "Carlos", "notas": [7, 7, 8]},
]

resultado = calcular_media(alunos)

for r in resultado:
    print(f"Nome: {r['nome']}, Média: {r['media']}, Situação: {r['situacao']}")