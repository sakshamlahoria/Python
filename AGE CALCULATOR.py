age=int(input('Enter your age '))
if age<=1:
    print("Infant Child")
elif age>1:
    if age<=18:
        print("Child")
    elif age>=19:
        if age<=60:
            print("Adult")
else:
    print("Senior Citizen")