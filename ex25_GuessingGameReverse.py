'''This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number.
As the writer of this program, you will have to choose how your program will strategically guess. 
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), 
and then increase / decrease by 1 as needed. After you’ve written the program, 
try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)'''

import random 

def GuessingGameReverse():
    attemps = 0
    maxis = 100
    mini = 0

    print('Think a number from 0 to 100. ')

    numberRandom = random.randint(mini, maxis)
    answer = ''

    while answer != 'c':

        answer = str(input('The number is {}? Answer me: '. format(numberRandom))).lower()
        attemps += 1

        if answer == 'b':
            mini = numberRandom + 1
            numberRandom = random.randint(mini, maxis)
        elif answer == 's':
            maxis = numberRandom - 1
            numberRandom = random.randint(mini, maxis) 
        elif answer == 'c':
            print(f'You did it. Congratulations!\n The number in my head was {numberRandom}\n\
            Number of attemps was {attemps}')
            break
        else:
            print('Invalid answer. Enter "c" or "b" or "s", please.')

def main():
    GuessingGameReverse()
if __name__ == "__main__":
    main()
main()