tarefas = []
def adicionar_tarefa(tarefas):
    descrição = input('Descreva a sua tarefa: ')
    prioridade = input('Prioridade da tarefa (Baixa, Média, Alta): ').lower()
    if prioridade not in ['baixa', 'média', 'alta']:
            print('Prioridade inválida.')
            return
            
    tarefas.append({
        'Descrição': descrição, 
        'Prioridade': prioridade, 
        'status': False
        })
    print('Tarefa Adicionada')
    
def listar_tarefas(tarefas):
    if not tarefas:    
        print('Não há tarefas.')
        return 'Não há tarefas.'
    for i, tarefa in enumerate(tarefas):
        status = 'Concluída' if tarefa['status'] else 'Pendente'
        print(f'ID[{i}] - [{tarefa['Prioridade'].capitalize()}] {tarefa['Descrição'].capitalize()} - [{status}]')
   
def concluir_tarefa(tarefas):
    if listar_tarefas(tarefas) == 'Não há tarefas.':
        return
    try:
        tarefa_id = int(input('Escolha o ID da tarefa que deseja concluir. (Use apenas números): '))
        if 0 <= tarefa_id < len(tarefas):
            tarefas[tarefa_id]['status'] = True
    except ValueError:
        print ('Entrada inválida.')
        return
def filtrar_tarefas(tarefas):
    if listar_tarefas(tarefas) == 'Não há tarefas.':
        return
    print('Filtrar por:\n1.Prioridade\n2.Status')
    escolha = int(input('Escolha a opçao(1,2): '))

    if escolha == 1:
        nivel = input('Prioridade (Baixa, Média, Alta)? ').lower()
        filtradas = [t for t in tarefas if t['Prioridade'] == nivel]
    elif escolha == 2:
        status = input('Pendente ou Concluída?').lower()
        desejado = False if status == 'pendente' else True
        filtradas = [t for t in tarefas if t['status'] == desejado]
    else:
        print('Opção inválida')
        return
    if not filtradas:
        print('Nenhuma tarefa encontrada com este filtro.')
        return
    listar_tarefas(filtradas)

while True:

    print('Gerenciador de Tarefas')

    print('1 - Adicionar Tarefa')
    print('2 - Listar Tarefas')
    print('3 - Concluir Tarefa')
    print('4 - Filtrar Tarefa')
    print('5 - Sair do Programa')

    try:
        escolha = int(input('Selecione a opção (1,2,3,4,5): ')) #Seria mais funcionnal com botões
    except ValueError:
        print('Digite 1,2,3,4 ou 5.')
        continue
    if escolha == 1:
        adicionar_tarefa(tarefas)
    
    elif escolha == 2:
      listar_tarefas(tarefas) 
    elif escolha == 3:
        concluir_tarefa(tarefas)
    elif escolha == 4:
        filtrar_tarefas(tarefas)
    elif escolha == 5:
        print('Encerrando...')
        break
    else:
        print('Entrada inválida.')
        