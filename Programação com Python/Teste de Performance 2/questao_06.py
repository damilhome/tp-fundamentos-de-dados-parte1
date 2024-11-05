'''
Faça um programa que leia um intervalo inferior e superior e mostre os números primos encontrados nesse intervalo.

Por exemplo, para o intervalo de 5 a 10, a saída será: 5, 7.
O programa também deve mostrar a quantidade de números primos encontrados.
Implemente uma função para verificar se um número é primo.
'''
import math

def prime_number_checker(num):
    '''
    Checks if the number is prime.

    Args:
        num (int): Number to check if it is prime.

    Returns:
        bool: A boolean 'True' if it is prime and a boolean 'False' if it is not prime.
    '''
    if(num < 2):
        return False
    elif(num == 2):
        return True

    num_sqrt = int(math.sqrt(num))

    for number in range(2, num_sqrt + 1):
        if(num % number == 0):
            return False
        
    return True

def print_primes(first_num, last_num):
    '''
    Prints the prime numbers of a sequence of numbers and the total of prime numbers found in the sequence.

    Args:
        first_num (int): First number of the sequence.
        last_num (int): Last number of the sequence.

    Returns:
        None.
    '''

    prime_numbers = []

    for num in range(first_num, last_num + 1):
        if(prime_number_checker(num)):
            prime_numbers.append(num)
    
    print(f'Prime numbers found: {prime_numbers}')
    print(f'Total of prime numbers found: {len(prime_numbers)}')

print_primes(0, 45)