'''
Faça um programa que leia uma sequência de números, terminada pelo número zero, e armazene-os em uma lista.

O programa deve mostrar apenas os números maiores ou iguais à média dos elementos lidos.
Implemente uma função para ler a lista e outra para exibir os números filtrados.
Utilize apenas os comandos ensinados em aula.
'''

def read_numbers():
    '''
    Request and store X numbers from the user and returns a list with it.

    Returns:
        list: A list with the numbers entered by the user.
    '''

    list = []

    while True:
        try:
            number = input('Enter a number or type "exit" to exit: ')
            if(number == 'exit'):
                break
            list.append(int(number))
        except:
            print('Non-numeric value entered')

    return list

def calculate_avarage(list):
    '''
    Calculate the avarage of a numerical list.

    Args:
        list (list): A numerical list.

    Returns:
        int: An integer representing the avarage of the values of the list.
    '''
    sum = 0
    for num in list:
        sum += num

    return sum // len(list)

def filter_list(list):
    '''
    Filter and print the values of a list that are equal or higher to it's avarage.

    Args:
        list (list): A numerical list.

    Returns:
        None.
    '''

    new_list = []
    avarage = calculate_avarage(list)

    for num in list:
        if(num >= avarage):
            new_list.append(num)

    print(new_list)

list_of_numbers = read_numbers()
filter_list(list_of_numbers)