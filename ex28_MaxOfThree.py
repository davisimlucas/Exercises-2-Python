'''
Implement a function that takes as input three variables, 
and returns the largest of the three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python normally takes care of for us. 
All you need is some variables and if statements!
'''
def MaxOfThree():
    while True:
        number1 = int(input('enter a number: '))
        number2 = int(input('enter a number: '))
        number3 = int(input('enter a number: '))

        if number1 > number2 and number1 > number3:
            print('bigger : {}'.format(number1))
        elif number2 > number3:
            print('bigger is: {}'.format(number2))
        else:
            print('bigger is: {}'.format(number3))

        question = str(input('Do you wanna play again? (y/n) '))
        if question == 'y':
            continue 
        if question == 'n':
            break
        
def main():
    MaxOfThree()

if __name__ == 'main':
    main()
main()