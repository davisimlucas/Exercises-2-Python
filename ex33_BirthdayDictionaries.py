import time

def birthday(dictionaryBirthday):
    print('Bem-vindo(a) ao dicionário de aniversários.')
    time.sleep(1)

    print('A pessoas que você possui como escolha são:')
    time.sleep(0.9)
    for name in dictionaryBirthday:
        print(name)
        time.sleep(0.9)

    choice = str(input('\nQuem você deseja descobrir a data de nascimento? \n'))
    
    if choice in dictionaryBirthday:
        print(f'A data de nascimento de {choice} é {dictionaryBirthday[choice]}')

dictionaryBirthday = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815",
    "Donald Trump": "06/14/1946",
    "Rowan Atkinson": "01/6/1955"
    }