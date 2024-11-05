'''
Faça um programa que leia um número do teclado e verifique se ele está presente na lista:
[20, 10, 30, 40, 60, 50, 70, 90, 80, 100].

Se o número for encontrado, o programa deve retornar sua posição na lista.
Caso contrário, deve retornar -1, indicando que o número não foi encontrado.
Implemente uma função para buscar o elemento na lista.
'''

LIST = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]

def read_number():
    '''Return a number typed by the user'''
    while True:
        try:
            return int(input('Enter a number: '))
        except:
            print('Non-numeric value entered.')

def find_number(list):
    '''
    Return index of a given number in the list or -1 if not found.

    Args:
        list (list): A list of numbers.

    Returns:
        int: The index of the given number or -1 if not found.
    '''

    number = read_number()

    try:
        return list.index(number)
    except:
        return -1
    
print(find_number(LIST))