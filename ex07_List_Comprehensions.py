'''
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
 Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''
import math
number = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# anexar somente os elementos pares numa lista nova
pares = [par for par in number if par % 2 == 0]
# anexar somente os ímpares numa nova lista
impares = [impar for impar in number if impar % 2 != 0]
# anexar numa nova lista o valor da radiciação de cada elemento da lista a
raiz = [math.pow(elemento, 0.5) for elemento in number]

print(f'{pares}\n{impares}\n{raiz}')
'''
Aprendizado: em list comprehensions o primeiro termo variável é o que entrará na lista no final..
'''

