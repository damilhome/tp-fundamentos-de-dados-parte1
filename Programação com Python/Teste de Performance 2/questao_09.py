'''
Faça um programa que leia uma sequência de números, terminada pelo número zero, e mostre-os na ordem invertida.

Implemente uma função para ler a lista de números e outra para exibir a lista invertida.
'''

#[11, 22, 33, 44, 55, 66, 77, 88]
def read_numbers():
    '''
    Request and store X numbers from the user and returns a list with it.

    Returns:
        list: A list with the numbers entered by the user.
    '''

    list = []

    while True:
        try:
            number = int(input('Enter a number (0 to exit): '))
            list.append(number)
            if(number == 0):
                break
        except:
            print('Non-numeric value entered.')

    return list

def invert_list():
    '''Prints a sequence of numbers typed by the user in a reversed order'''
    list = read_numbers()
    print(list[::-1])

invert_list()
