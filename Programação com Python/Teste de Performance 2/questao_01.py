def vowel_counter(characters_sequence):
    '''
    Counts the number of vowels in a character sequence.

    Args:
        characters_sequence (str): The character sequence.

    Returns:
        int: The number of vowels in the character sequence.
    '''

    vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'î', 'ô', 'û', 'ã', 'õ', 'ä', 'ë', 'ï', 'ö', 'ü']
    number = 0

    for character in characters_sequence:
        if (character.lower() in vowels): 
            number += 1 
    
    return number

characters_sequence = input('Type the characters sequence: ')
print(vowel_counter(characters_sequence))