'''
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5
Concepts:
Lists
More conditionals (if statements)
'''
import statistics

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

menores5 = []
for i in a:
    if i < 5:
        menores5.append(i)
print(menores5)

# melhor alternativa ---> List Comprehensions
menores5_ = [x for x in a if x < 5]
print(menores5_)

# cálculo da média dos elementos da list 
mean = statistics.mean(a)
print(f'A média da lista a = {mean:.2f}')