'''
Uma progressão aritmética (PA) é uma sequência numérica onde cada termo, a partir do segundo, é igual à soma do termo anterior com uma constante.

A constante é a diferença entre o segundo e o primeiro número.
Faça um programa que receba dois números inteiros e, a partir dessa informação, gere uma sequência em PA.
'''
try:
    LAST_TERM = int(input('Digite quantos termos deseja na progressão: '))
    FIRST_TERM = int(input('Digite o primeiro termo da progressão: '))
    SECOND_TERM = int(input('Digite o segundo termo da progressão: '))

    def arithmetic_progression(first_term, second_term):
        '''
        Calculates a arithmetic progression from first_term to LAST_TERM.

        Args:
            first_term (int): The first term of the arithmetic progression.
            second_term (int): The second term of the arithmetic progression.

        Returns:
            list: A list with the arithmetic progression.
        '''

        current_term = 3
        constant = second_term - first_term
        arithmetic_progression_list = [first_term, second_term]

        while current_term <= LAST_TERM:
            arithmetic_progression_list.append(first_term + ((current_term - 1) * constant))
            current_term += 1

        return arithmetic_progression_list

    print(arithmetic_progression(FIRST_TERM, SECOND_TERM))
except:
    print('Valor não numérico digitado.')