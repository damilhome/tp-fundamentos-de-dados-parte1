'''
Faça um programa que leia uma data no formato “dd/mm/aaaa” e mostre o dia, mês e ano no formato “dia de nome_do_mês de ano”. 
'''

def ler_data():
    '''
    Pede ao usuário para digitar uma data no formato dd/mm/aaaa.

    Returns
        str: uma data no formato dd/mm/aaaa.
    '''

    data = input('Digite uma data no formato dd/mm/aaaa: ')

    data_list = data.split('/')
    if(len(data_list) != 3):
        print('Data inválida.')
        return ler_data()
    elif(len(data_list[0]) != 2):
        print('Data inválida.')
        return ler_data()
    elif(len(data_list[1]) != 2):
        print('Data inválida.')
        return ler_data()
    elif(len(data_list[2]) != 4):
        print('Data inválida.')
        return ler_data()
    
    return data

def formatar_data():
    '''Recebe do usuário uma data no formato dd/mm/aaaa e a imprime no formato “dia de nome_do_mês de ano”.'''
    
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dia, mes, ano = ler_data().split('/')
    print(f'{dia} de {meses[int(mes) - 1]} de {ano}')

formatar_data()
