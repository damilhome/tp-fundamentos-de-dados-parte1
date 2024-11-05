'''
Faça um programa que some as seguintes listas:
[1, 2, 3, 4, 5, 6, 7, 8]
[10, 20, 30, 40, 50, 60, 70, 80]

Mostre o resultado da soma em uma terceira lista.
Exemplo:
A soma das listas seria:
[11, 22, 33, 44, 55, 66, 77, 88]
'''

def sum_list(list1, list2):
    '''
    Returns the sum of the values of two lists

    Args:
        list1 (list): First numerical list.
        list2 (list): Second numerical list.
    
    Returns:
        list: The list with the sum of the values of the two lists.
    '''

    list3 = []

    for index, num in enumerate(list1):
        list3.append(num + list2[index])

    return list3

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [10, 20, 30, 40, 50, 60, 70, 80]
print(sum_list(list1, list2))