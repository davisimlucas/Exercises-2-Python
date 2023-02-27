'''
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
Extras:
Use binary search.
Topics:
Booleans - True and False
Equality testing
Binary search
'''
import math 

def elementSearch(list, number):
    # iniciar com os índices "left" e "right" iguais a zero e o tamanho da lista - 1
    left, right = 0, len(list) - 1
    # laço while para sempre quando o número da esquerda for menor ou igual que o da direita
    while left <= right:
        # cálculo do índice do meio entre o esquedo e direito sempre aproximando-o para baixo (math.floor())
        mean = math.floor((left + right)/ 2)
        if list[mean] == number:
            # se o elemento que está na posição do meio for igual ao número fornecido, é verdade
            return True
        elif list[mean] < number:
            # se o número na posição do meio for menor, procure na direita do meio 
            left = mean + 1
        else: 
            # se o número na posição do meio for maior, procure na esquerda do meio
            right = mean - 1
    # caso não ache o número em nenhuma das hipóteses, significa que não se encontra na lista
    return False

# declarar uma list qualquer 
list_ = [number for number in range(1, 30, 2)]
numberProvided = int(input('Enter a number: '))
# chamar a função declarando os devidos parâmetros 
result = elementSearch(list_, numberProvided)
print(f'{list_}\n{result}')

