precos = [1000, 1200, 1245, 1251]

def imposto(preco):
    return preco * 1.1

precos_impostos = map(imposto, precos)
print (precos_impostos)
precos_impostos = list(map(imposto, precos))
print(precos_impostos)