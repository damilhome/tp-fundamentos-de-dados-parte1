'''
Faça um programa que leia um número do teclado e garanta que ele seja maior ou igual a zero.

Enquanto a entrada não for válida, o programa deve exibir uma mensagem de erro e pedir uma nova entrada.
'''

def read_number():
    '''Reads and returns a number greater than or equal zero from the user's keyboard.'''

    while True:
        try:
            number = int(input('Enter a number greater or equal zero: '))
            if(number < 0):
                print('Invalid number.')
                continue
            return number
        except:
            print('Non-numeric value entered.')

print(read_number())