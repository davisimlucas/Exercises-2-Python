'''
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 
For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
Concepts:
More about strings.
'''
def reverseWordOrder(variableString):
    '''
    utilizar da função join() para a união das strings sepanrando-as por " ", e da função split() que retorna
    uma lista de substrings
    --> transforma a frase string em lista através do split(), começa-la pelo último item pelo [::-1] e junta-la com o join()
    [::-1] = começa pelo último item e caminha até o primeiro de uma lista. 
    '''
    return print(" ".join(variable.split()[::-1]))

string: str = 'My name is Davi'
reverseWordOrder(string)
