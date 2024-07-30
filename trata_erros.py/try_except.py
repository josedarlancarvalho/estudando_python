# resumo_try_except.py

"""
Resumo sobre try e except em Python.
"""

# A estrutura try/except em Python é usada para lidar com exceções (erros) que podem ocorrer durante a execução do código.
# Isso permite que você "capture" erros específicos e responda a eles de maneira controlada, sem interromper o programa.

# Sintaxe básica
try:
    # bloco de código onde pode ocorrer uma exceção
    x = 10 / 0
except ZeroDivisionError:
    # bloco de código a ser executado se uma exceção ocorrer
    print("Você tentou dividir por zero!")

# Output: Você tentou dividir por zero!

# Exemplo com múltiplas exceções
try:
    x = int(input("Digite um número: "))
    y = 10 / x
except ZeroDivisionError:
    print("Você não pode dividir por zero!")
except ValueError:
    print("Você precisa digitar um número válido!")

# Capturando a exceção e a mensagem de erro
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Ocorreu um erro: {e}")

# Output: Ocorreu um erro: division by zero

# Bloco else e finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Você tentou dividir por zero!")
else:
    # Executado se nenhuma exceção ocorreu no bloco try
    print("Divisão bem-sucedida!")
finally:
    # Executado sempre, independentemente de uma exceção ter ocorrido ou não
    print("Bloco finally executado.")

# Output:
# Divisão bem-sucedida!
# Bloco finally executado.

# Exceções personalizadas
class MeuErro(Exception):
    pass

def verificar_valor(valor):
    if valor < 0:
        raise MeuErro("O valor não pode ser negativo!")

try:
    verificar_valor(-1)
except MeuErro as e:
    print(f"Erro personalizado capturado: {e}")

# Output: Erro personalizado capturado: O valor não pode ser negativo!

# Exemplos práticos
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except IOError:
        print("Erro ao ler o arquivo.")

# Tentando ler um arquivo inexistente
ler_arquivo("arquivo_inexistente.txt")

# Output: Arquivo não encontrado.

# Este resumo cobre os conceitos principais e exemplos de uso das estruturas try e except em Python.
# Você pode copiar e colar este código em um arquivo para estudar e testar no seu ambiente de desenvolvimento Python.
