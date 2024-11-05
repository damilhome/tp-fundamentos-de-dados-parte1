'''
Faça um programa que leia uma sequência de números, terminada pelo número zero, e mostre-os na ordem invertida.

Implemente uma função para ler a lista de números e outra para exibir a lista invertida.
'''

def print_list(list):
    '''prints a list'''
    print(list)

def invert_list(list):
    '''Reads a list and prints it reversed'''
    print_list(list[::-1])

invert_list([11, 22, 33, 44, 55, 66, 77, 88])