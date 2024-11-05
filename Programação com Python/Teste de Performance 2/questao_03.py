'''
Faça um programa que leia uma sequência de números inteiros positivos, terminada por zero. Para cada número lido, mostre seu fatorial.
Implemente uma função para o cálculo do fatorial.
'''

def factorial(num):
    '''
    Calculates the factorial of a number (num).

    Args:
        num (int): The number to calculate the factorial.

    Returns:
        int: The factorial of num.
    '''

    if(num == 0 or num == 1):
        return 1
    
    factorial = 0

    while(num > 1):
        if(factorial == 0):
            factorial = num * (num - 1)
            num -= 1
            continue
        factorial *= (num - 1)
        num -= 1
    
    return factorial

def display_factorial(sequence):
    '''
    Reads and displays the factorial of each number in a sequence of integers.

    Args:
        sequence (list): The sequence of integers.

    Returns:
        None.
    '''

    for num in sequence:
        print(f'Factorial of {num}: {factorial(num)}')

sequence = [5, 4, 3, 2, 1, 0]
display_factorial(sequence)