import time
import json 
from collections import *

dictionaryBirthdayJson = {}
with open("articles\ex35_fileJSON.json", "r") as content:
    dictionaryBirthdayJson = json.load(content)

while True:
    question = str(input("Deseja adicionar alguma pessoa no arquivo json? (sim/não) ")).title()
    time.sleep(1)
    if question == 'Sim':
        nameAdd = str(input('Entra com um nome: '))
        ageAdd = str(input('{} nasceu em: '.format(nameAdd)))
        dictionaryBirthdayJson[nameAdd] = ageAdd
        with open('articles\ex35_fileJSON.json', 'w') as file:
            json.dump(dictionaryBirthdayJson, file)
        time.sleep(1)
        print(f'A pessoa adicionada é {nameAdd} tendo nascida em {ageAdd}.\n')
    elif question == 'Não':
        break

convertString = {
    1: 'janeiro',
    2: 'fevereiro',
    3: 'março',
    4: 'abril',
    5: 'maio',
    6: 'junho',
    7: 'julho',
    8: 'agosto',
    9: 'setembro',
    10: 'outubro',
    11: 'novembro',
    12: 'dezembro'
}
mouths = []
for name, birthdayString in dictionaryBirthdayJson.items():
    mouth = int(birthdayString.split('/')[1])
    mouths.append(convertString[mouth])

result = Counter(mouths)
print(f'\n{result}\n')

