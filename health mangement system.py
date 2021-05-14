def getdate():
    import datetime
    return datetime.datetime.now()
print("what file you would like to work on hammad, saksham or rohan")
user=int(input("enter 1 2 or 3"))
if user==1:
    print("in which file do you want to perform: Diet or Exercises")
    a=(input("enter your choice"))
    if a=="diet":
        print("you are in hammad's diet file")
        c=input("what action do you want to perform LOAD or RETRIVE")
        if c== "load":
            f=open("hammad_diet.txt","a")
            b=input("write your data here")
            b=f.write(b)
        elif c=="retrive":
            f=open("hammad_diet.txt")
            print(f.readlines())
    elif a=="exercises":
        print("you are in hammad's exercises file")
        c=input("what action do you want to perform LOAD or RETRIVE")
        if c== "load":
            f=open("hammad_exercises.txt","a")
            b=input("write your data here")
            b=f.write(b)
        elif c=="retrive":
            f=open("hammad_exercises.txt")
            print(f.readlines())
        else:
            print("you have given a wrong input")

elif user==2:
    print("in which file do you want to perform: Diet or Exercises")
    a=(input("enter your choice"))
    if a=="diet":
        print("you are in saksham's's diet file")
        c=input("what action do you want to perform LOAD or RETRIVE")
        if c== "load":
            f=open("saksham_diet.txt","a")
            b=input("write your data here")
            b=f.write(b)
        elif c=="retrive":
            f=open("saksham_diet.txt")
            print(f.readlines())
    elif a=="exercises":
        print("you are in saksham's exercises file")
        c=input("what action do you want to perform LOAD or RETRIVE")
        if c== "load":
            f=open("saksham_exercise.txt","a")
            b=input("write your data here")
            b=f.write(b)
        elif c=="retrive":
            f=open("saksham_exercise.txt")
            print(f.readlines())
        else:
            print("you have given a wrong input")

elif user== 3:
    print("in which file do you want to perform: Diet or Exercises")
    a=(input("enter your choice"))
    if a=="diet":
        print("you are in rohan's diet file")
        c=input("what action do you want to perform LOAD or RETRIVE")
        if c== "load":
            f=open("rohan_diet.txt","a")
            b=input("write your data here")
            b=f.write(b)
        elif c=="retrive":
            f=open("rohan_diet.txt")
            print(f.readlines())
    elif a=="exercises":
        print("you are in rohan's exercises file")
        c=input("what action do you want to perform LOAD or RETRIVE")
        if c== "load":
            f=open("rohan_exercises.txt","a")
            b=input("write your data here")
            b=f.write(b)
        elif c=="retrive":
            f=open("rohan_exercises.txt")
            print(f.readlines())
        else:
            print("you have given a wrong input")
else:
    print("you entered a wrong input")

