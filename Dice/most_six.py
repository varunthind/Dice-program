import random


while True:
    diceNo = random.randint(1, 6)
    randNo = random.randint(1, 6)
    otherRand = random.randint(1, 6)
    roll = input('Press Enter(play) Or Space and then Enter(exit):')
    if roll == 'close' or roll == ' ' or roll == 'exit':
        exit()
    elif randNo == diceNo or randNo == otherRand:
        print(6)
    else:
        print(diceNo)
