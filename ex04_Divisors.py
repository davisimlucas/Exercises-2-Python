'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''

number =  int(input('Insira um número: '))
'''
divisors = []
for divisor in range(1, number + 1):
    if number % divisor == 0:
        divisors.append(divisor)
'''
divisors = [divisor for divisor in range(1, number + 1) if number % divisor == 0] #number+1: para considerar a divisão por ele mesmo

print(f'O divisores de {number} são: {divisors}')
