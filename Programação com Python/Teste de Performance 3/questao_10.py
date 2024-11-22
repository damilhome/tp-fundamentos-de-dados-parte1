def solicitar_numero():
    '''Solicita ao usuário um número entre 1 e 7.
    
    Returns
        int: Um número entre 1 e 7.
    '''

    try:
        numero = int(input('Digite um número entre 1 e 7: '))
    except:
        print('Valor não numérico digitado.')
        return solicitar_numero()
    
    if(numero < 1 or numero > 7):
        print('Número inválido.')
        return solicitar_numero()
    else:
        return numero
    
def encontrar_dia_semana(dia):
    '''
    Encontra o dia da semana correspondente a um número recebido.
    
    Args
        dia (int): Um número entre 1 e 7 correspondente a um dia da semana.
    
    Returns
        str: O dia da semana correspondente ao número.
    '''

    dias_da_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]

    return dias_da_semana[dia - 1]

print(encontrar_dia_semana(solicitar_numero()))