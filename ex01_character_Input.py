'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Concepts: 
Getting user input
Manipulating strings
'''
name = str(input('Insira o nome da pessoa: '))
age = int(input('Insira a idade: '))

diference = int(100 - age)
print(f'Ainda faltam {diference} anos para que {name} chegue aos 100 anos.\n')

question = str(input('Deseja adicionar dados de outras pessoas? '))

while question == 'Sim':
    name = str(input('Insira o nome da próxima pessoa: ')) 
    age = int(input('Insira a idade dela: '))
    diference = int(100 - age)

    print(f'Ainda faltam {diference} anos para que {name} chegue aos 100 anos.\n')

    question = str(input('Deseja adicionar dados de outras pessoas? '))


    









