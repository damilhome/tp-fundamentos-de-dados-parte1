'''
Faça um programa que leia uma sequência de nomes de alunos de uma turma, terminada por "FIM", além de suas duas notas (entre 0 e 10).

Para cada aluno, o programa deve informar:
    Média do aluno
    Se o aluno está aprovado ou em prova final (Média ≥ 6 = Aprovado).
Ao final, o programa deve mostrar a média geral da turma.
Utilize a função de arredondamento para exibir as médias.
Implemente as funções:
    Entrada do nome e das notas.
    Cálculo da média do aluno.
    Cálculo da média da turma.
'''

AVARAGE_FOR_APPROVAL = 6

def get_name():
    '''Reads and returns a name entered by the user.'''

    return input('\nEnter a name or "FIM" para sair: ')

def get_grade():
    '''Reads and returns a numerical value representing a grade entered by the user.'''

    while True:
        try:
            number = int(input('Enter a grade: '))
            if(number < 0):
                print('Grade needs to be greater than or equal to zero.')
                continue
            return number
        except:
            print('Non-numeric value entered.')

def student_avarage(grade1, grade2):
    '''
    Calculates the avarage of a student grade.
    
    Args:
        grade1 (int): The student's first grade. 
        grade2 (int): The student's second grade. 

    Returns:
        float: Float value representing the student's avarage.
    '''

    return (grade1 + grade2) / 2

def is_approved(avarage):
    '''
    Checks if the student is approved or not
    
    Args:
        avarage (int): The student avarage grade.

    Returns:
        bool: 'True' if student is approved and 'False' if not approved.
    '''

    return avarage >= AVARAGE_FOR_APPROVAL

def class_avarage(list_of_grades):
    '''
    Calculates the avarage of the class.
    
    Args:
        list_of_grades (list): A list with all student's avarages.

    Returns:
        float: Float value representing the class' avarage.
    '''

    sum = 0
    for num in list_of_grades:
        sum += num
    return sum / len(list_of_grades)

def get_students_informations():
    '''
    Request the student's name and grades and provides a list with all students information.

    Returns:
        list: A list with a list for each student's informations as: [name, grade 1, grade 2].    
    '''
    students = []
    student = []

    while True:
        name = get_name()
        if(name.upper() == 'FIM'):
            break
        grade1 = get_grade()
        grade2 = get_grade()

        student.append(name)
        student.append(grade1)
        student.append(grade2)
        students.append(student)
        student = []

    return students

def print_students_and_class_situation(students):
    '''
    Prints the student's situation and class avarage.

    Args:
        students (list): A list with a list for each student's information as [name, grade 1, grade 2]

    Returns:
        None.
    '''

    class_grades = []

    for stu in students:
        avarage = student_avarage(stu[1], stu[2])
        class_grades.append(avarage)
        situation = 'Aprovado' if is_approved(avarage) else 'Prova final'

        print(f"\n{stu[0]}'s avarage: {avarage}")
        print(f'Student situation: {situation}')

    print(f'\nClass avarage: {class_avarage(class_grades)}')

def main():
    '''Organizes the calls of functions and flow of the program.'''

    students = get_students_informations()
    print_students_and_class_situation(students)

main()