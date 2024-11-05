'''
Faça um programa que, a partir da lista:
[10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
crie duas listas: uma com números pares e outra com números ímpares.

Implemente uma função para determinar se um número é par ou ímpar.
'''

LIST = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

def is_odd(num):
    '''Returns 'True' if number is odd and 'False' if even.'''

    if(num % 2 == 0):
        return False
    return True

def even_odd_lists(list):
    '''
    Creatres and returns two lists, one with only even numbers and other with only odd numbers.

    Args:
        list (list): A numerical list.

    Returns:
        list: A first list with even numbers and a second with odd numbers.
    '''

    even = []
    odd = []

    for num in list:
        if(is_odd(num)):
            odd.append(num)
        else:
            even.append(num)

    return even, odd

even, odd = even_odd_lists(LIST)
print(f'Even numbers: {even}')
print(f'Odd numbers: {odd}')