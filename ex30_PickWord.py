'''
In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 
Download this file and save it in the same directory as your Python code. 
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. 
Each line in the file contains a single word.
'''
import random
import articles

def pickWord():
    # gerar lista vazia que receberá todos os nomes do arquivo txt 
    words = []
    # leitura de todos os nomes que estão no arquivo txt ---> "r" == read mode
    with open('articles\ex30_sowpods.txt') as f:
        # definir a variável line que lerá o nome que estão no arquivo txt
        # readline() retorna o valor da linha
        # strip() retorna uma cópia de string
        line = f.readline().strip()
        while line:
            line = f.readline().strip()
            words.append(line)

    # número que vai representar o index da list words sendo sorteado entre 0 e o tamanho (len()) da list 
    randomWord = random.randint(0, len(words))
    pickedWord = words[randomWord]
    
    return pickedWord





