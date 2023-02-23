'''
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''
from ex10_ListOverlapComprehensions import ListOverlap
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# transformar as lists para sets, pois sets evitam duplicações
set_a = set(a) # = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
set_b = set(b) # = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
ListOverlap(a, b)
elementsCommon = list(set_a & set_b)     # "&": and = o que há nos dois
print(elementsCommon)