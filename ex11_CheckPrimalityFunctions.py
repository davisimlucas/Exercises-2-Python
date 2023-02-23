''' 23/02/2023
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
Concepts for this week:
Functions
Reusable functions
Default arguments
'''
number = int(input('Insira um número: '))
def checkPrimality(variable):
    contPrimality = 0       # conta quantas vezes o número divido pelo x iguala o resto igual a zero
    contNotPrimality = 0    # conta quantas vezes o número dividido por x iguala o resto igual a zero

    # para ser número primo ele é somente divisível por 1 e por ele mesmo
    for x in range(2, variable - 1):
        if variable % x != 0:
            contPrimality =+ 1 
        else:
            contNotPrimality =+ 1   

    if contPrimality != 0 and contNotPrimality == 0: 
        print(f'{variable} é um numero primo! ')
    else:
        print(f'{variable} não é um número primo!')
    
checkPrimality(number)