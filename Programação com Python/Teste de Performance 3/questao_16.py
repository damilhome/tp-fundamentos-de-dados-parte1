'''
Faça um programa que leia dois números e mostre a média dos números lidos.
Utilize a formatação “f-strings” para a exibição da saída.
'''

def ler_numero():
    '''
    Lê um número digitado pelo usuário.
    
    Returns
        int: Um número digitado pelo usuário.
    '''
    while True:
        try:
            numero = int(input('Digite um número: '))
            break
        except:
            print('Valor não numérico digitado.')
    
    return numero

def calculo_media():
    '''Exibe a média entre dois números digitados pelo usuário'''

    num_1 = ler_numero()
    num_2 = ler_numero()

    print(f'A média de {num_1} e {num_2} é {(num_1 + num_2) / 2}')

calculo_media()