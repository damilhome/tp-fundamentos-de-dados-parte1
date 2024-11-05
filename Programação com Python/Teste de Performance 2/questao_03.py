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

def read_numbers():
    '''
    Request and store X numbers from the user and returns a list with it.

    Returns:
        list: A list with the numbers entered by the user.
    '''

    list = []

    while True:
        try:
            number = int(input('Enter a number higher than zero (0 to exit): '))
            if(number < 0):
                print('Number smaller than zero')
                continue
            list.append(number)
            if(number == 0):
                break
        except:
            print('Non-numeric value entered.')

    return list

def display_factorial():
    '''
    Request numbers from the user and displays the factorial of each number.

    Returns:
        None.
    '''

    sequence = read_numbers()

    for num in sequence:
        print(f'Factorial of {num}: {factorial(num)}')

display_factorial()