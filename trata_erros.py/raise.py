# resumo_raise.py

"""
Resumo sobre a palavra-chave 'raise' em Python.
"""

# A palavra-chave `raise` em Python é usada para lançar exceções.
# Isso permite que você gere manualmente uma exceção em seu código.
# `raise` é frequentemente usado em conjunto com tratamento de exceções para manipular erros de forma mais eficaz.

# Exemplo básico
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Você não pode dividir por zero!")
    return a / b

# Testando a função com divisão por zero
try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(f"Erro: {e}")

# Output: Erro: Você não pode dividir por zero!

# Exemplo com exceções personalizadas
class NumeroNegativoError(Exception):
    pass

def raiz_quadrada(x):
    if x < 0:
        raise NumeroNegativoError("Você não pode calcular a raiz quadrada de um número negativo!")
    return x ** 0.5

# Testando a função com número negativo
try:
    resultado = raiz_quadrada(-4)
except NumeroNegativoError as e:
    print(f"Erro: {e}")

# Output: Erro: Você não pode calcular a raiz quadrada de um número negativo!

# Relevância e usos práticos
# `raise` é útil para:
# - Sinalizar que algo deu errado em seu programa.
# - Impedir que seu programa continue a execução em um estado inválido.
# - Criar mensagens de erro personalizadas que ajudam a depurar seu código.
# - Definir e lançar suas próprias exceções personalizadas para cenários específicos.

# Exemplo de exceções aninhadas
def processar_dados(dados):
    try:
        if not isinstance(dados, list):
            raise TypeError("Os dados devem ser uma lista!")
        if not dados:
            raise ValueError("A lista de dados não pode estar vazia!")
        # Processamento fictício dos dados
        return [x * 2 for x in dados]
    except TypeError as e:
        print(f"Erro de tipo: {e}")
        raise
    except ValueError as e:
        print(f"Erro de valor: {e}")
        raise

# Testando a função com dados inválidos
try:
    resultado = processar_dados("não é uma lista")
except Exception as e:
    print(f"Erro capturado no nível superior: {e}")

# Output:
# Erro de tipo: Os dados devem ser uma lista!
# Erro capturado no nível superior: Os dados devem ser uma lista!

# Testando a função com lista vazia
try:
    resultado = processar_dados([])
except Exception as e:
    print(f"Erro capturado no nível superior: {e}")

# Output:
# Erro de valor: A lista de dados não pode estar vazia!
# Erro capturado no nível superior: A lista de dados não pode estar vazia!

# Este resumo cobre os principais conceitos e exemplos de uso da palavra-chave `raise` em Python.
# Você pode copiar e colar este código em um arquivo para estudar e testar no seu ambiente de desenvolvimento Python.
