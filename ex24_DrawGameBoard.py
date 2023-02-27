'''
Time for some fake graphics! Let’s say we want to draw game boards that look like this:
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
'''
# entrar com o tamanho do tabuleiro
boardSize = int(input('Enter a board size: '))

# função para gerar linhas horizontais 
def horizontaLine():
    # printa " --- " vezes boardSize mais 1
    print(' --- ' * boardSize)

# função para gerar linhas verticais
def verticalLine():
    # printa "|  " vezes boardSize mais 1
    print('|   ' * (boardSize + 1))

# for looping para o index para percorrer o número do tamanho
# obs: tem que usar o comando range pois boardSize é um int (não iterável)
for index in range(boardSize):
    # index gera uma linha de cada função
    horizontaLine()
    verticalLine()
# linha vertical de baixo
print(horizontaLine())





