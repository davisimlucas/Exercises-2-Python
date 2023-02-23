'''
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
Concepts to practice:
Lists and properties of lists
List comprehensions (maybe)
Functions
'''
import random
a = [5, 10, 15, 20, 25]
randomList = [random.randint(0, 100) for x in range(random.randint(1, 100))]
def listEnds(List):
    print(List)
    newList = [List[0], List[-1]]
    print(newList)

listEnds(randomList)