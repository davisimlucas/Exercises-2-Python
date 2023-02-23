'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Concepts:
Modular arithmetic (the modulus operator)
Conditionals (if statements)
Checking equality
'''

number = int(input('Insira um número: '))

if number % 2 == 0:
    print(f'{number} é par!')
else:
    print(f'{number} é ímpar!')

if number % 4 == 0:
    print(f'{number} também é múltiplo por 4')
else:
    pass

question = str(input('Deseja adicionar outro número? (Sim ou Não)'))
while question == 'Sim':
    number = int(input('Insira outro número: '))
    if number % 2 == 0:
        print(f'{number} é par!')
    else:
        print(f'{number} é ímpar!')

    if number % 4 == 0:
        print(f'{number} também é múltiplo por 4')
    else:
        pass
    question = str(input('Deseja adicionar outro número? (Sim ou Não)'))

    
 



