import random

while True:
    diceNo = random.randint(1, 6)
    randNo = random.randint(1, 6)
    roll = input('Press Enter(play) Or Space and then Enter(exit):')
    roll.lower()
    if roll == 'close' or roll == ' ' or roll == 'exit':
        exit()
    elif randNo == diceNo:
        print(6)
    else:
        print(diceNo)
