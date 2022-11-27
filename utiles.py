
import random
def playgame():
    game = input("do you want to play game?")
    if game == "y":
        rand = random.randint(0, 9)
        print(rand)
        return (rand)

    else:
        exit(0)
