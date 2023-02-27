'''
As you may have guessed, we are trying to build up to a full tic-tac-toe board. 
However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
'''

def checkingGameTicTacToe(game):

    # verificação das linhas
    for line in game:
        # line será uma lista
        if line.count(1) == 3:
            return print('Winner is player 1')
        elif line.count(2) == 3:
            return print('Winner is player 2')

    # verificação da colunas por índice pois mudarão as sublistas na análise
    for col in range(3):
        columns = [game[line][col] for line in range(3)]
        if columns.count(1) == 3:
            return print('Winner is player 1')
        elif columns.count(2) == 3:
            return print('Winner is player 2')

    # verificação das diagonais:
    diag1 = [game[i][i] for i in range(3)]
    diag2 = [game[i][2-i] for i in range(3)]
    if diag1.count(1) == 3 or diag2.count(1) == 3:
        return print('Winner is player 1')
    elif diag1.count(2) == 3 or diag2.count(2) == 3:
        return print('Winner is player 2')

    # caso não haja vercedor ainda:
    return print('No winners yet')

game = [
    [2, 0, 1],
    [2, 1, 0],
    [2, 0, 0]
    ]
checkingGameTicTacToe(game)

        
