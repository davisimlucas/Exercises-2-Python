'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
'''
question = str(input('Deseja jogar pedra, papel e tesoura? (s/n)')).lower()

while question == 's':

    player1 = str(input('Jogador 1, qual sua jogada? ')).lower()    # .lower() -> converte em letra minúscula.
    player2 = str(input('Jogador 2, qual sua jogada? ')).lower()

    if player1 == 'pedra':
        if player2 == 'tesoura':
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')

    elif player1 == 'tesoura':
        if player2 == 'papel':
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')

    elif player1 == 'papel':
        if player2 == 'pedra':
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')

    else: 
        print('Jogadas inválidas, tente novamente.')
        continue

    question = str(input('Deseja jogar novamente? (s/n)')).lower()
    
