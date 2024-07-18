Exercício: Sistema de Gerenciamento de Tarefas
Crie um programa que gerencie uma lista de tarefas. O programa deve ter uma função principal chamada gerenciar_tarefas que exiba um menu com as seguintes opções:

Adicionar Tarefa
Remover Tarefa
Listar Tarefas
Sair
Cada tarefa deve ser representada por um dicionário com as seguintes chaves:

titulo: Título da tarefa
descricao: Descrição da tarefa
concluida: Estado da tarefa (True ou False)
Requisitos:

A função adicionar_tarefa deve permitir ao usuário adicionar uma nova tarefa.
A função remover_tarefa deve permitir ao usuário remover uma tarefa pelo título.
A função listar_tarefas deve exibir todas as tarefas e seu estado (Concluída ou Não Concluída).
A função concluir_tarefa deve permitir ao usuário marcar uma tarefa como concluída pelo título.
Você deve usar estruturas de repetição e condição para implementar o menu e as funcionalidades.

Função adicionar_tarefa:

Pede ao usuário o título e a descrição da tarefa.
Cria um dicionário para a tarefa e a adiciona à lista de tarefas.

Função remover_tarefa:

Pede ao usuário o título da tarefa a ser removida.
Remove a tarefa da lista se encontrada.

Função listar_tarefas:

Exibe todas as tarefas e seu estado (Concluída ou Não Concluída).

Função concluir_tarefa:

Pede ao usuário o título da tarefa a ser marcada como concluída.
Marca a tarefa como concluída se encontrada.

Função gerenciar_tarefas:

Exibe o menu e chama as funções apropriadas com base na escolha do usuário.