'''
Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, 
letter by letter. The player guesses one letter at a time until the entire word has been guessed. 
(In the actual game, the player can only guess 6 letters incorrectly before losing).
Let’s say the word the player has to guess is “EVAPORATE”. 
For this exercise, write the logic that asks a player to guess a letter and displays letters in the 
clue word that were guessed correctly.
For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - 
we will deal with those in a future exercise.
'''

from ex30_PickWord import pickWord
 
word = pickWord()
def hangman(variable):
    wordList = list(variable)
    attempts = 0
    spaceWord = ['_' for i in range(len(wordList))]
    # for looping que itera index e acompanha cada elemento da lista da palavra com a função enumerate()
    for index, letter in enumerate(wordList): 
        while spaceWord.count("_") != 0:
            letterInput = str(input('Enter a letter: ')).upper()

            if letterInput in wordList:
                # se constar: fazer iterar cada posição (i) acompanhado a letra (l) com a função enumerate() na lista da palavra 
                for i, l in enumerate(wordList):
                    if l == letterInput:
                        # se for: o elemento naquela posição(i) deixa de ser "_" e se recebe agora letra inserida 
                        spaceWord[i] = letterInput
                print(f'You pick a right letter!\n\
                    {"".join(map(str, spaceWord))}')

            elif letterInput not in wordList:
                print('Incorrect! Try again.\n') 
            attempts += 1
            
    print(f'You got the word right! With {attempts} attempts\n')
              
