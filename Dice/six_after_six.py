# This program will return six again-and-again after five  numbers(plays)
import random

num = 1
while True:
    diceNo = random.randint(1, 6)
    roll = input('Press Enter(play) Or Space and then Enter(exit):')
    if roll == 'close' or roll == ' ' or roll == 'exit':
        exit()
    elif num == 6:
        print(6)
        num = 0
    else:
        print(diceNo)
    num += 1
