import taf
tarefas = []
while True:

    print('Gerenciador de Tarefas')

    print('1 - Adicionar Tarefa')
    print('2 - Listar Tarefas')
    print('3 - Concluir Tarefa')
    print('4 - Filtrar Tarefa')
    print('5 - Sair do Programa')

    try:
        escolha = int(input('Selecione a opção (1,2,3,4,5): '))
    except ValueError:
        print('Digite 1,2,3,4 ou 5.')
        continue
    if escolha == 1:
        taf.adicionar_tarefa(tarefas)

    elif escolha == 2:
      taf.listar_tarefas(tarefas) 

    elif escolha == 3:
        taf.concluir_tarefa(tarefas)

    elif escolha == 4:
        taf.filtrar_tarefas(tarefas)

    elif escolha == 5:
        taf.print('Encerrando...')
        break

    else:
        print('Entrada inválida.')
        