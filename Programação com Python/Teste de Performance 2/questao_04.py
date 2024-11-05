'''
Faça um programa que mostre a tabuada dos números de 1 a 10.
'''

FIRST = 1
LAST = 10

def addition_table():
    '''Displays de addition table of FIRST to LAST.'''

    for num1 in range(FIRST, LAST + 1):
        print(f'\nTable of {num1}')
        for num2 in range(FIRST, LAST + 1):
            print(f'{num1} + {num2} = {num1 + num2}')

def subtraction_table():
    '''Displays the subtraction table of FIRST to LAST.'''

    for num1 in range(FIRST, LAST + 1):
        print(f'\nTable of {num1}')
        for num2 in range(FIRST, LAST + 1):
            if(num2 < num1):
                continue
            print(f'{num2} - {num1} = {num2 - num1}')

def multiplication_table():
    '''Displays the multiplication table of FIRST to LAST.'''

    for num1 in range(FIRST, LAST + 1):
        print(f'\nTable of {num1}')
        for num2 in range(FIRST, LAST + 1):
            print(f'{num1} x {num2} = {num1 * num2}')

def division_table():
    '''Displays the division table of FIRST to LAST.'''

    for num1 in range(FIRST, LAST + 1):
        print(f'\nTable of {num1}')
        for num2 in range(FIRST, LAST + 1):
            if(num2 < num1):
                continue
            if(num1 == 1):
                print(f'{num2} / {num1} = {num2 // num1}')
            elif(num1 % 2 == 0 and num2 % 2 == 0):
                print(f'{num2} / {num1} = {num2 // num1}')
            elif(num1 % 2 != 0 and num2 % 2 != 0):
                print(f'{num2} / {num1} = {num2 // num1}')

addition_table()
subtraction_table()
multiplication_table()
division_table()