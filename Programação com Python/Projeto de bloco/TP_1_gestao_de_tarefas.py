from datetime import date, datetime

def print_menu():
    '''Imprime todas as opções do menu para o usuário.'''

    print(
'''
############ MENU ############
[1] - Adicionar nova tarefa
[2] - Listar tarefas pendentes
[3] - Concluir uma tarefa
[4] - Remover uma tarefa
[0] - Sair
'''
    )

def get_user_numerical_input():
    '''
    Solicita ao usuário um valor numérico representando a opção desejada do menu.

    Returns:
        int: Um valor numérico representando a escolha do usuário para o menu.
    '''

    while True:
        try:
            opcao = int(input('Escolha uma opção: '))
            print()
            return opcao
        except:
            print('Valor não numérico digitado.')

def formatar_data_final(data):
    '''
    Transforma uma data em string no formato 'dia/mês/ano' para um objeto datime no formato 'dia/mês/ano'.

    Args:
        data (str): Uma string com uma data no formato 'dia/mês/ano'.

    Returns:
        datetime: Um objeto datetime com a data no formato 'dia/mês/ano'.
    '''

    mascara_ptbr = '%d/%m/%Y'
    return datetime.strptime(data, mascara_ptbr).date()

def adicionar_data_final():
    '''
    Retorna uma data digitada pelo usuário no formato 'dia/mês/ano'.

    Returns:
        datetime: Um objeto datetime com a data no formato 'dia/mês/ano'.
    '''

    while True: 
        data = input('Digite a data para concluir a tarefa (dia/mês/ano): ') 
        nova_data = data.split('/') 
        if len(nova_data) == 3: 
            dia, mes, ano = nova_data 
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                break 
            else: 
                print('Formato de data inválido. Certifique-se de usar apenas números.') 
        else:
            print('Formato de data inválido. Use o formato dia/mês/ano.')

    return formatar_data_final(data)

def adicionar_tarefa(total_tarefas):
    '''
    Solicita todas as informações de uma nova tarefa para criar um objeto tarefa.

    Args:
        total_tarefas (int): Um int representando o total de tarefas já adicionadas.

    Returns:
        dict: Um dicionário contendo todas as informações de uma nova tarefa.
    '''

    tarefa = {}

    tarefa['id'] = total_tarefas + 1
    tarefa['titulo'] = input('Digite o título da tarefa: ')
    tarefa['descricao'] = input('Digite a descrição da tarefa: ')
    tarefa['data_criacao'] = date.today()
    tarefa['status'] = 'Pendente'
    tarefa['data_concluir'] = adicionar_data_final()
    tarefa['prioridade'] = input('Prioridade (baixa, média, alta): ')

    return tarefa

def imprimir_tarefa(tarefa):
    '''
    Imprime uma tarefa.

    Args:
        tarefa (dict): Um dicionário contendo a tarefa com os atributos:
                    - id (int): Identificador único da tarefa. 
                    - titulo (str): Título da tarefa.  
                    - descricao (str): Descrição detalhada da tarefa. 
                    - data_criacao (datetime): Data de criação da tarefa. 
                    - status (str): Status atual da tarefa (e.g., 'Pendente', 'Concluída'). 
                    - data_concluir (datetime): Data limite para concluir a tarefa. 
                    - prioridade (str): Nível de prioridade da tarefa (e.g., 'alta', 'média', 'baixa').
    
    Returns:
        None.
    '''

    print(
            f'''
Id da tarefa: {tarefa['id']}
Título: {tarefa['titulo']}
Descrição: {tarefa['descricao']}
Data de criação: {tarefa['data_criacao']}
Data para concluir: {tarefa['data_concluir']}
Prioridade: {tarefa['prioridade']}
Status: {tarefa['status']}
'''
        )


def listar_tarefas(lista_tarefas):
    '''
    Imprime cada tarefa de uma lista de tarefas.

    Args:
        lista_tarefas (list): Uma lista de dicionários contendo todas as tarefas. 
                            Cada tarefa possui as seguintes chaves: 
                            - id (int): Identificador único da tarefa. 
                            - titulo (str): Título da tarefa.  
                            - descricao (str): Descrição detalhada da tarefa. 
                            - data_criacao (datetime): Data de criação da tarefa. 
                            - status (str): Status atual da tarefa (e.g., 'pendente', 'concluída'). 
                            - data_concluir (datetime): Data limite para concluir a tarefa. 
                            - prioridade (str): Nível de prioridade da tarefa (e.g., 'alta', 'média', 'baixa').
    
    Returns:
        None.
    '''

    print('############ TAREFAS ############')
    for tarefa in lista_tarefas:
        imprimir_tarefa(tarefa)

def concluir_tarefa(lista_tarefas):
    '''
    Altera o status de uma terafa para 'Concluída'.

    Args:
        lista_tarefas (list): Uma lista de dicionários contendo todas as tarefas. 
                            Cada tarefa possui as seguintes chaves: 
                            - id (int): Identificador único da tarefa. 
                            - titulo (str): Título da tarefa.  
                            - descricao (str): Descrição detalhada da tarefa. 
                            - data_criacao (datetime): Data de criação da tarefa. 
                            - status (str): Status atual da tarefa (e.g., 'pendente', 'concluída'). 
                            - data_concluir (datetime): Data limite para concluir a tarefa. 
                            - prioridade (str): Nível de prioridade da tarefa (e.g., 'alta', 'média', 'baixa').
            
        Returns:
            None.
    '''

    while True:
        try:
            id = int(input('Digite o id da tarefa para concluir ou -1 para cancelar: '))

            if(id == -1):
                break

            concluida = False
            for tarefa in lista_tarefas:
                if(tarefa['id'] == id):
                    tarefa['status'] = 'Concluída'
                    print('Tarefa marcada como concluída.')
                    concluida = True
                    break

            if(not concluida):
                print(f'Nenhuma tarefa com id {id} encontrada.')
            
            if(concluida):
                break
            
        except:
            print('Valor não numérico digitado.')


def remover_tarefa(lista_tarefas):
    '''
    Remove uma tarefa da lista de tarefas.

    Args:
        lista_tarefas (list): Uma lista de dicionários contendo todas as tarefas. 
                            Cada tarefa possui as seguintes chaves: 
                            - id (int): Identificador único da tarefa. 
                            - titulo (str): Título da tarefa.  
                            - descricao (str): Descrição detalhada da tarefa. 
                            - data_criacao (datetime): Data de criação da tarefa. 
                            - status (str): Status atual da tarefa (e.g., 'pendente', 'concluída'). 
                            - data_concluir (datetime): Data limite para concluir a tarefa. 
                            - prioridade (str): Nível de prioridade da tarefa (e.g., 'alta', 'média', 'baixa').
            
    Returns:
        None.
    '''

    while True:
        try:
            id = int(input('Digite o id da tarefa para remover ou -1 para cancelar: '))

            if(id == -1):
                break

            removida = False
            for tarefa in lista_tarefas:
                if(tarefa['id'] == id):
                    lista_tarefas.remove(tarefa)
                    print('Tarefa removida com sucesso.')
                    removida = True
                    break

            if(not removida):
                print(f'Nenhuma tarefa com id {id} encontrada.')
            
            if(removida):
                break
            
        except:
            print('Valor não numérico digitado.')


def main():
    '''Organiza a chamada das funções e o fluxo do programa.'''
    
    lista_tarefas = []
    total_tarefas = 0

    while True:
        print_menu()
        user_chocie = get_user_numerical_input()

        match user_chocie:
            case 1:
                lista_tarefas.append(adicionar_tarefa(total_tarefas))
                total_tarefas += 1
            case 2:
                listar_tarefas(lista_tarefas)
            case 3:
                concluir_tarefa(lista_tarefas)
            case 4:
                remover_tarefa(lista_tarefas)
            case 0:
                break
            case _:
                print('Opção inválida.')

        
main()