def solicitar_cpf():
    '''
    Solicita que o usuário digite um CPF válido.
    
    Returns
        str: Um CPF válido digitado pelo usuário.
    '''
    try:
        cpf = int(input('Digite um CPF (somente número): '))
    except:
        print('Digite apenas números.')
        return solicitar_cpf()
    
    cpf = str(cpf)
    if(len(cpf) == 11):
        return cpf
    else:
        print('CPF inválido.')
        return solicitar_cpf()
    
def formatar_cpf(n):
    '''
    Formata um CPF para o formato 999.999.999-99.
    
    Args
        n (str): Um CPF válido, de 11 dígitos.

    Returns
        str: Um CPF no formato 999.999.999-99.
    '''

    return f'{n[0]}{n[1]}{n[2]}.{n[3]}{n[4]}{n[5]}.{n[6]}{n[7]}{n[8]}-{n[9]}{n[10]}'

print(formatar_cpf(solicitar_cpf()))