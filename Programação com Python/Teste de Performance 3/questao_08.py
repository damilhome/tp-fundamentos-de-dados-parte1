def solicitar_frase():
    '''Solicita que o usuário digite uma frase.
    
    Returns
        str: a frase digitada pelo usuário.
    '''
    return input('Digite uma frase: ')

def verificar_quantidade_vogais(frase):
    '''
    Verifica a quantidade de vogais presente em uma frase.

    Args
        frase (str): A frase a ser verificada.

    Returns
        int: A quantidade de vogais presente na frase.
    '''
    vogais = ['a', 'e', 'i', 'o', 'u']
    sum = 0

    for vogal in vogais:
        quantidade = frase.lower().count(vogal)
        print(quantidade)
        sum += quantidade
    
    return sum

def vogais_na_frase():
    '''Inicia o sistema de contagem de vogais na frase.'''

    frase = solicitar_frase()
    quantidade_vogais = verificar_quantidade_vogais(frase)

    print(f'{frase} possui {quantidade_vogais} vogais.')

vogais_na_frase()