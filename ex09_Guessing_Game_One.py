'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
'''
import random
# input de um número inteiro 
number = int(input('Insira um número: '))
# defnição da função que realiza o jogo
def guessingGameOne(variable):
    #comando para execução do sorteio --> random.randint() ---> importar biblioteca random
    randomNumber = random.randint(1, 9)     
    print(f'O número sorteado é {randomNumber}.')
    while True:
        # obs ---> valor absoluto (módulo) = abs()
        if variable == randomNumber:
            resposta = str('Você acertou! Parabéns!')
            print(resposta)
            break # caso o usuário acerte de primeira, o laço while e if termina.
        elif 0 < abs(variable - randomNumber) <= 4:
            resposta = str('Você quase acertou. Tente novamente.')
            print(resposta)
        elif 3 < abs(variable - randomNumber) <= 9:
            resposta = str('Errou, tente novamente.')
            print(resposta)
        elif variable < 1 or variable > 9:
            print('Dados inválidos.')
            continue
        # perguntar para o usuário se deseja tentar jogar novamente.
        question = str(input('Deseja tentar novamente? (s/n) ')).lower()
        if question == 's':
            variable = int(input('\nInsira um número: '))
            randomNumber = random.randint(1, 9)     
            print(f'O número sorteado é {randomNumber}.')
        else: 
            break
# chamar a função que realiza o jogo atribuindo outra variável externa como parâmetro
guessingGameOne(number)







