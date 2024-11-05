'''
Faça um programa que calcule a soma e a média dos números de 1 a 100.
'''

FIRST = 1
LAST = 101

def sum_and_avarage():
    '''
    Calculates the sum and average of the number from FIRST to LAST.

    Returns:
        int: The sum of numbers from FIRST to LAST.
        float: The avarage of the numbers from FIRST to LAST.
    '''

    sum = 0

    for num in range(FIRST, LAST):
        sum += num

    avarage = sum / (LAST - 1)

    return sum, avarage

sum, avarage = sum_and_avarage()
print(f'Sum: {sum}, Avarage: {avarage}')