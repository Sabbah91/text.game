while True:
    answer= input('Do you wanna play a Game ? (yes/no)  ')
    if answer.lower().strip() ==  "yes":
        answer = input("You enter a cave and there 2 paths (left/right) you have to choose one :")
        if answer=="left":
            print('Suddenly a DRAGON appear , And you are Fucked  up')
            print('You lose try again (GAME OVER )')
        elif answer=="right":
            print (' you took the correct path ')
            print('Congrats YOU MADE IT (WE HAVE A WINNER)')
    else:
        print('Then Fuck off')