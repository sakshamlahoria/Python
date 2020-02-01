import math,random
import pyttsx3 as tts
s=tts.init()
def register():

    fname=input('enter your name')
    add=input('enter your address')
    ph=input('enter your phone no.')
    mname=input('enter your mother name')
    faname=input('enter your father name')
    password=input('enter your password')
    adharno=" "
    digits="1234567890"
    for i in range(13):
        adharno +=digits[math.floor(random.random() * 10)]



    f=open(adharno ,"a")
    f.write(fname +",")
    f.write(add + ",")
    f.write(ph+ ",")
    f.write(mname+ ",")
    f.write(faname+ ",")
    f.write(adharno + ",")
    f.write(password + "\n")
    s.say("your aadhar has been registered")
    s.runAndWait()
    f.close()

def login():
    adharno=input("enter aadhar number:")
    p = input("enter password")
    f=open(adharno ,"r")
    flag=1
    for i in f:
        j=i.split(",")
        w=j[6]
        plen=len(w)-1
        w=w[0:plen]
        if w==p:
            print("welcome")
            flag=1
            s.say("login successfully")
            s.runAndWait()
            break
        else:
            flag=0
    if flag==0:
        print("wrong input")
choice="y"
while choice=='y':
    print("1.register")
    print("2.login")
    ch=int(input("enter your choice"))
    if ch==1:
        register()
    elif ch==2:
        login()
    else:
        print("invalid input")
    choice=input("wanna continue?(y/n)")