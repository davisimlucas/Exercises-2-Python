'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)

Concepts: 
list indexing
string are list
'''

phrase = []    
while True:
    word = input('Insira uma palavra, caso seja "end", termina a frase. \n')
    if word == 'end':
        break
    else:
        phrase.append(word)

def Palindrome(variable):
    phraseComplete = "".join(variable)
    phraseCompleteSpaces = " ".join(variable)
    reversePhrase = phraseComplete[::-1]
    reversePhraseComplete = "".join(reversePhrase)
    reversePhraseCompleteSpaces = " ".join(reversePhrase)
    print(f'A frase escrita é: {phraseCompleteSpaces}\nSeu inverso é: {reversePhraseCompleteSpaces}')

    if phraseComplete == reversePhraseComplete:
        print('É um palíndromo.')
    else:
        print('Não é palíndromo.')
    
Palindrome(phrase)






