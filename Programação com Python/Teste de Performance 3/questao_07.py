'''
Faça um programa que o usuário entre com uma palavra e verifique se a mesma é palíndromo. 
'''

def verificar_palindromo(palavra):
    '''Verifica se uma palavra digitada pelo usuário é um palindromo.
    
    Args
        palavra (str): A palavra para a ser verificada.

    Returns
        bool: True se a palavra é palindromo e False se não for palindromo.
    '''
    
    return True if palavra.lower() == palavra[::-1].lower() else False

def solicitar_palavra():
    '''Solicita que o usuário digite uma palavra.
    
    Returns
        str: a palavra digitada pelo usuário.
    '''
    return input('Digite uma palavra: ')

def palindromo():
    '''Inicia o sistema verificador de palíndromo.'''
    palavra = solicitar_palavra()
    e_palindromo = verificar_palindromo(palavra)

    if(e_palindromo):
        print(f'{palavra} é um palíndromo.')
    else:
        print(f'{palavra} não é um palíndromo.')

palindromo()