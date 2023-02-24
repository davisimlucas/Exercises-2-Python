'''
Write a program (function!) that takes a list and returns a new list that contains all 
the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
Concepts: 
Sets
'''

def ListRemoveDuplicate_1(list_):
    set_list = set(list_)
    return print(list(set_list))

def ListRemoveDuplicate_2(list_):
    # criar lista vazia que receberá os elementos da lista que estiver na variável.
    sets = []      
    # percorrer todos os elementos dessa lista variável. 
    for i in list_:
        # verificar se o elemento não existe na lista 'sets', caso exista, não entrará, evitando duplicatas. 
        if i not in sets:
            # se o elemento não existe, entrará na lista 'sets'a
            sets.append(i)
    return print(sets)

a = [1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 10]

ListRemoveDuplicate_1(a) # = [1, 2, 3, 4, 5, 6, 7, 8, 10]
ListRemoveDuplicate_2(a) # = [1, 2, 3, 4, 5, 6, 7, 8, 10]







