'''
Faça um programa que leia uma sequência de caracteres terminada por um ponto (.) e mostre o número de vogais digitadas.
Cada caractere deve ser digitado/lido separadamente.
'''

def vowel_counter():
    '''
    Ask the user for a character and returns the number of vowels typed.

    Returns:
        int: The number of vowels typed by the user.
    '''
    
    characters_sequence = ''

    while True:
        character = input('Type a character (or \e to exit): ')
        
        if(character == '\e'):
            break
        else:
            characters_sequence += character

    vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'î', 'ô', 'û', 'ã', 'õ', 'ä', 'ë', 'ï', 'ö', 'ü']
    number = 0

    for character in characters_sequence:
        if (character.lower() in vowels): 
            number += 1 
    
    return number

print(f'Number of vowels: {vowel_counter()}')