'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. 
Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
Concepts:
Random
Functions 
main method
'''
import random 

def CowsAndBulls():

    attempts = 0
    while True:
        # entrada do seu número
        numberChoice = input('Enter a number with 4 digites (type "quit" to end):\n>>> ')
        # caso o usuário deseja sair, somente escrver "quit"
        if numberChoice == 'quit':
            print('Goodbye!')
            break

        # list comprehensions para gerar uma lista com cada elemento do número digitado pelo usuário
        numberChoiceList = [int(number_) for number_ in numberChoice]

        # list comprehensions para gerar lista de números aleatórios (import random)
        numberRandomList = [random.randint(0, 9) for _ in range(4)]

        cows = 0
        bulls = 0
        # looping for para um número variável (index) percorrer o tamanho (len()) da lista de Random 
        for index in range(len(numberRandomList)):
            # estrutura if para verificar se o número digitato numa posição é o mesmo número gerado no random na mesma posição
            if numberChoiceList[index] == numberRandomList[index]:
                cows += 1
            elif numberChoiceList[index] in numberRandomList:
                bulls += 1

        # para cada tentativa, aumenta a contagem de "attemps"
        attempts += 1

        print(f'Number random: {"".join(map(str, numberRandomList))}\n\
        Cow`s number: {cows}\n\
        Bull`s number: {bulls}\n\
        Attemp`s number: {attempts}')

        # estrutura if para caso o usuário acerte o número sortedo, o laço while termine
        if cows == 4:
            break

        # estrutura if para verificar se o usuário deseja continuar no jogo
        question = input('Try again: (y/n)\n').lower()
        if question == 'y':
            continue
        elif question == 'n':
            break 

def main():
    CowsAndBulls()

if __name__ == '__main__':
    main()

        