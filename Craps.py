import random

def dice_roll ():
    pause = input("press <Enter> to roll the dice.")
    roll = random.randrange(6)+1 + random.randrange(6)+1
    print("you rolled a", roll)
    return roll

def main():
    response = input("do you want to play craps (y/n)?")
    if response == "y":
        instructions = input("do you need instructions (y/n?)")
        if instructions == "y":
            print("instructions.")
    while response == "y":
        firstroll = dice_roll()
        if firstroll == 7 or firstroll == 11:
            print("you won!")
        elif firstroll == 2 or firstroll == 3 or firstroll == 12:
            print("you lose!")
        else:
            print("let's try to roll the point.")
            point = firstroll
            newroll = dice_roll()
            while newroll != point and newroll != 7:
                newroll = dice_roll()
            if newroll == point:
                print("you won!")
            else:
                print("you lose!")
        response = input("do you want to play again (y/n)?")
    print("okay, see you next time!")


if __name__ == "__main__":
    main()
