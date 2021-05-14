# snake,water,gun
import random
i=0
user1=0
comp1=0
print("for every tie match both players will be credited 1 point")
while i<=9:
    lst=["snake", "water", "gun"]
    choice=random.choice(lst)
    user=input("enter your choice first")
    i=i+1
    if user==choice:
        print(choice)
        print("tie")
        user1=user1+1
        comp1=comp1+1
        print("your score=",user1)
        print("bot score=",comp1)
    elif user=="snake":
        if choice== "water":
            print(choice)
            comp1=comp1+1
            print("you lose")
            print("bot score =",comp1)
            print("your score=",user1)
        elif choice=="gun":
            print(choice)
            comp1=comp1+1
            print("you lose")
            print("bot score =",comp1)
            print("your score=",user1)
        else:
            print("you had taken a wrong choice")
    elif user=="water":
        if choice=="snake":
            print(choice)
            print("you won")
            user1=user1+1
            print("your score=",user1)
            print("bot score =",comp1)

        elif choice=="gun":
            print(choice)
            print("you won")
            user1=user1+1
            print("your score=",user1)
            print("bot score =",comp1)
        else:
            print("you had taken a wrong choice")
    elif user=="gun":
        if choice=="snake":
            print(choice)
            print("you won")
            user1=user1+1
            print("your score=",user1)
            print("bot score =",comp1)

        elif choice=="water":
            print(choice)
            comp1=comp1+1
            print("you lose")
            print("bot score =",comp1)
            print("your score=",user1)
        else:
            print("you had taken a wrong choice")
    else:
        print("you entered a wrong choice")
if comp1==user1:
    print("it's a tie match")
elif comp1>user1:
    print("bot won this match")
elif comp1<user1:
    print("you won this match")
else:
    pass