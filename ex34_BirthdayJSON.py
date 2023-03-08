import json 
from ex33_BirthdayDictionaries import birthday

while True:
    question = str(input('Digite uma ação: Add ou Find ou Sair \n')).title()

    dictionaryBirthdayJson = {}
    with open("articles\ex34_fileJSON.json", "r") as f:
        # json.load() lê o arquivo e o converte em object 
        dictionaryBirthdayJson = json.load(f)

    def add(dictionaryBirthdayJson):
        nameAdd = str(input('Digite um nome: ')).title()
        birthdayAdd =  str(input('Quando {} nasceu? '.format(nameAdd)))
        dictionaryBirthdayJson[nameAdd] = birthdayAdd
        with open("articles\ex34_fileJSON.json", "w") as file:
            json.dump(dictionaryBirthdayJson, file)
        print(f'A pessoa adicionada foi {nameAdd} tendo seu nascimento no dia {birthdayAdd}')

    if question == 'Sair':
        False
    elif question == 'Add':
        add(dictionaryBirthdayJson)
    elif question == 'Find':
        birthday(dictionaryBirthdayJson)






