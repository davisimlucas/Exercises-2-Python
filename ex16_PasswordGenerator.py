'''
Write a password generator in Python. Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
Concepts: 
Python's random module
'''
import random

def passwordGenerator():
    # gerar todas as listas de todos os elementos que serão usados para compor as senhas
    alfabeto_m = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 's', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
    # upper() => letras maiúsculas das strings
    alfabeto_M = [letra.upper() for letra in alfabeto_m]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    caracteres = ['!','@', '$', '%', '&', '*', '+', '_']

    while True:
        type_of_Password = str(input('Senha forte ou fraca? ')).lower()

        password = []
        if type_of_Password == 'fraca':
            # cada item da senha vai percorrer de um até ou 4 ou 5 ou 6
            for valorEasy in range(1, random.randint(4, 6)):
                #itens da senha irão ser retirados aleatoriamente das listas de alfabeto_m e numbers pelo função choice()
                valorEasy = random.choice(alfabeto_m) or random.choice(numbers)
                password.append(valorEasy)
            # O primeiro item da senha será uma letra maiúscula tirada aleatoriamente da lista 
            password[0] = random.choice(alfabeto_M) + password[0] # colocar como soma pois o elemento [0] é vazio, não podendo adicionar por index

        elif type_of_Password == 'forte':
            for valorStrong in range(1, random.randint(10, 12)):
                valorStrong = random.choice(alfabeto_m) or random.choice(numbers) or ramdom.choice(caracteres)
                password.append(valorStrong)
            password[0] = random.choice(alfabeto_M) + password[0]   # colocar como soma pois o elemento [0] é vazio, não podendo adicionar por index
            password[-1] = password[-1] + random.choice(caracteres) # colocar como soma pois o elemento [-1] é vazio, não podendo adicionar por index
            password[-2] = password[-2] + random.choice(numbers)
            password[-3] = password[-3] + random.choice(numbers)
        else:
            print('Digite para essa questão "fraco" ou "forte".') # caso não seja digitada a resposta requerida, volte no início do laço while
            continue
        # função join() somente junta strings, como a senha pode possuir integers, converte-los usando o comando map()
        print(F'A senha gerada é: {"".join(map(str, password))}\n')

        question = str(input('Deseja criar uma nova senha? (s/n) ')).lower()
        # caso deseja criar uma nova senha, o "continue" fará voltar para o início do laço while
        if question == 's':
            continue
        else: # caso não, o break fará sair do laço while
            print(f'Sua senha continua sendo {"".join(map(str, password))}\n')    
            break
passwordGenerator()