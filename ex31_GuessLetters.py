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

# fazer com que a palavra sorteada venha do ex 30 
word = pickWord()
# definir função com parâmetro variável
def hangman(variable):
    # transformar cada letra da palavra numa lista de strings
    wordList = list(variable)
    attempts = 0
    # gerar lista que recebe elementos vazios ("_") do tamanho da lista que está a palavra
    spaceWord = ['_' for i in range(len(wordList))]
    # for looping que itera index e acompanha cada elemento da lista da palavra com a função enumerate()
    for index, letter in enumerate(wordList):
        # laço while para repetir a jogada até que não exista mais espaços vazios ("_") na list spaceWord 
        while spaceWord.count("_") != 0:
            # input para o usuário inserir uma letra
            # diretamente essa letra é convertida em maiúsculas
            letterInput = str(input('Enter a letter: ')).upper()
            # estrutura condicional para verificar se a letra inserida consta na lista da palavra sorteada
            if letterInput in wordList:
                # se constar: fazer iterar cada posição (i) acompanhado a letra (l) com a função enumerate() na lista da palavra 
                for i, l in enumerate(wordList):
                    # estrutura condicional para verificar se a letra l na lista e na posição(i) é igual a letra inserida
                    if l == letterInput:
                        # se for: o elemento naquela posição(i) deixa de ser "_" e se recebe agora letra inserida 
                        spaceWord[i] = letterInput
                # caso a letra inserida consta na lista da palavra
                print('You pick a right letter!\n')
                # função join() para imprimir a cada letra inserida a evolução do usuário no jogo
                print(''.join(map(str, spaceWord)))
            # caso a letra inserida não conste na lista da palavra 
            elif letterInput not in wordList:
                print('Incorrect! Try again.\n') 
            attempts += 1
    # caso exista algum "_" na lista spaceWord, sai do laço while 
    print(f'You got the word right! With {attempts} attempts\n')
              



