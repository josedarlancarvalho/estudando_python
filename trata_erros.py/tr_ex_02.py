'''Exercício 2: Leitura de Arquivo com Tratamento de Erros
Escreva um programa que tenta ler o conteúdo de um arquivo. Se o arquivo não existir ou ocorrer um erro durante a leitura, o programa deve exibir uma mensagem apropriada.
Passos:
Solicite ao usuário o nome de um arquivo.
Tente abrir e ler o arquivo.
Exiba o conteúdo do arquivo se a leitura for bem-sucedida.
Use try e except para tratar:
Arquivo não encontrado.
Outros erros de I/O.'''

try:
    nome_arquivo = input("Digite o nome do arquivo: ")
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
except PermissionError:
    print("Erro: Você não tem permissão para abrir este arquivo.")
except Exception as e:
    print(f"Erro desconhecido: {e}")
