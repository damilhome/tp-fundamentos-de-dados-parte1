'''
Faça um programa que mostre o menor, o maior, a soma e a média dos elementos da lista:
[10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

Utilize apenas os comandos ensinados em aula.
'''

LIST = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

def find_higher(list):
    '''Returns the higher value in a numerical list'''

    higher = 0

    for num in list:
        if(num > higher):
            higher = num

    return higher

def find_smallest(list):
    '''Returns the smallest number in a numerical list.'''

    smaller = 0

    for i, num in enumerate(list):
        if(i == 0):
            smaller = num
        else:
            if(num < smaller):
                smaller = num
    
    return smaller

def sum_list(list):
    '''Returns the sum of the values of a numerical list.'''
    sum = 0
    for num in list:
        sum += num
    return sum


def list_avarage(list):
    '''Returns the avarage of the values of a numerical list.'''
    return sum_list(list) // len(list)


def main(list):
    print(f'Higher: {find_higher(list)}')
    print(f'Smaller: {find_smallest(list)}')
    print(f'Sum: {sum_list(list)}')
    print(f'Avarage: {list_avarage(list)}')

main(LIST)