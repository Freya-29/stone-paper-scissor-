import random
def gameWin(comp , you):
    if comp == you:
        return None
    elif comp == 'st':
        if you == 'pa':
            return True
        elif you == 'sc':
            return False
    elif comp == 'pa':
        if you == 'sc':
            return True
        elif you == 'st':
            return False
    elif comp == 'sc':
        if you == 'st':
            return True
        elif you == 'pa':
            return False


while True:
    randNo = random.randint(1, 3)
    # print(randNo)
    if randNo == 1:
        comp = 'st'
    elif randNo == 2:
        comp = 'pa'
    elif randNo == 3:
        comp = 'sc'

    print("your's Turn: Stone(st) Paper(pa) scissors(sc) ? ")
    you = input("--> ")
    a = gameWin(comp, you)
    print(f"You choose {you}")
    print(f"computer choose {comp}")

    if a == None:
        print("The game is tie!")
    elif a:
        print("Hurrah....You Win!")
    else:
        print("Try again..You Lose!")

    print("Enter any key to play more")
    print("or Press 'n' for exit")
    i = input()
    if (i == 'n'):
        break


