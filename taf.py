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
        if 0 <= tarefa_id < len(tarefas): #Verifica se o ID não excede as tarefas
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