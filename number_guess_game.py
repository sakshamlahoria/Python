n=100
guess=11
g=0
while(True):
    guess=guess-1
    if guess-1<=10:
        print("you have ",guess, "chances left")

        if guess<=0:
            print("GAME OVER")
            break


    a=int(input("guess the number"))
    if a==100:
        print("you guessed the number right and you took" , 11-guess,"number of guesses to finish this game")
        break
    elif a>100:
        print("its lesser than this number")
    else:
        print("its bigger than this number")