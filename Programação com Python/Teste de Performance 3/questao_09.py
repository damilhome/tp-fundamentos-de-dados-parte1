def solicitar_numero_telefone():
    '''
    Solicita que o usuário digite um número de telefone de 11 dígitos.
    
    Returns
        str: Um número de telefone de 11 dígitos digitado pelo usuário.
    '''
    try:
        telefone = int(input('Digite um número de telefone de 11 dígitos (somente número): '))
    except:
        print('Digite apenas números.')
        return solicitar_numero_telefone()
    
    telefone = str(telefone)
    if(len(telefone) == 11):
        return telefone
    else:
        print('Número de telefone inválido.')
        return solicitar_numero_telefone()
    
def formatar_numero_telefone(n):
    '''
    Formata um número de telefone digitado pelo usuário para o formato (99) 99999-9999.
    
    Args
        n (str): Um número de telefone de 11 dígitos.

    Returns
        str: Um número no formato (99) 99999-9999.
    '''

    return f'({n[0]}{n[1]}) {n[2]}{n[3]}{n[4]}{n[5]}{n[6]}-{n[7]}{n[8]}{n[9]}{n[10]}'

print(formatar_numero_telefone(solicitar_numero_telefone()))