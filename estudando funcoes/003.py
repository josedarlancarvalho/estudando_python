'''Crie uma função chamada eh_palindromo que verifica se uma palavra é um palíndromo 
(palavra que se lê da mesma forma de trás para frente). A função deve retornar True se
 for um palíndromo e False caso contrário.'''
def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False
palindromo('teste')
print(palindromo('arara'))
a = 'darlan'
print(f"a palavra {a} é palindromo? {palindromo(a)}")
b = 'arara'
print(f"a palavra {a} é palindromo? {palindromo(b)}")