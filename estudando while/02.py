n = int(input("digite um numero: "))
soma = 0
while n > 0:
    digito = n % 10 # entra 93 > 93%10 {9} > sobrou 3 > 9 + resto(3)
    soma += digito
    n = n // 10
print(soma)