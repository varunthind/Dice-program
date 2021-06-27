import random

while True:
    diceNo = random.randint(1, 6)
    roll = input('Press Enter(play) Or Space and then Enter(exit):')
    if roll == 'close' or roll == ' ' or roll == 'exit':
        exit()
    else:
        print(diceNo)
