'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence 
is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
Concepts: 
Functions
'''
def Fibonnaci(variable):
    list_fib = [0, 1]
    for number in range(1, variable):
        list_fib.append(list_fib[-1] + list_fib[-2])
    return ", ".join(map(str, list_fib[:variable]))

fibNumber = int(input('Quantos números da sequência você quer gerar? '))
print(Fibonnaci(fibNumber))


