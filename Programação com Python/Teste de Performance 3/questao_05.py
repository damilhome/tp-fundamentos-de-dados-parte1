'''
Refaça o programa anterior de forma validar a data, verificando os meses com 31, 30, 29, e 28 dias, além do mês ser válido. 
Exemplo: Para a entrada “29/02/2024”, o programa deverá exibir “data válida”. Para a entrada “29/02/2023”, o programa deverá exibir “data inválida”.
'''

def verificar_validade_data(data):
    '''
    Valida se o dia e mês são válidos de acordo com o calendário.

    Args:
        data (str): uma string representando uma data.
    
    Returns:
        bool: False se inválida, True se válida.
    '''

    dia, mes, ano = data.split('/')
    dia = int(dia)
    mes = int(mes)
    trinta_um = [1, 3, 5, 7, 8, 10, 12]
    trinta = [4, 6, 9, 11]

    if(mes < 1 or mes > 12):
        return False
    elif(mes in trinta_um):
        if(dia < 1 or dia > 31):
            return False
    elif(mes in trinta):
        if(dia < 1 or dia > 30):
            return 
    else:
        if(dia < 1 or dia > 29):
            return False
    
    return True

def validar_formato_data(data):
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
    elif(len(data_list[0]) != 2):
       return False
    elif(len(data_list[1]) != 2):
       return False
    elif(len(data_list[2]) != 4):
       return False
    return True

def formatar_data():
    '''Imprime separadamente o dia, mês e ano da data digitada pelo usuário no formato dd/mm/aaaa.'''
    data = input('Entre com a data (dd/mm/aaaa): ')
    if(not validar_formato_data(data) or not verificar_validade_data(data)):
        print('Data inválida.')
        return formatar_data()
    dia, mes, ano = data.split('/')
    print(int(dia))
    print(int(mes))
    print(int(ano))

formatar_data()