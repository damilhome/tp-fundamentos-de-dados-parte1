'''
Faça um programa que leia uma data no formato “dd/mm/aaaa” e mostre o dia, mês e ano no formato de inteiros.
'''

def validar_data(data):
    '''
    Valida se uma data está no formato 'dd/mm/aaaa'

    Args:
        data (str): uma string representando uma data.
    
    Returns:
        bool: False se inválida, True se válida.
    '''
    data_list = data.split('/')
    if(len(data_list) != 3):
        return False
    if(len(data_list[0]) != 2):
       return False
    if(len(data_list[1]) != 2):
       return False
    if(len(data_list[2]) != 4):
       return False
    return True

def formatar_data():
    '''Imprime separadamente o dia, mês e ano da data digitada pelo usuário no formato dd/mm/aaaa.'''
    data = input('Entre com a data (dd/mm/aaaa): ')
    if(not validar_data(data)):
        print('Data inválida.')
        return formatar_data()
    dia, mes, ano = data.split('/')
    print(int(dia))
    print(int(mes))
    print(int(ano))

formatar_data()