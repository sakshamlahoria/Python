import sqlite3
def admin1():
    db = sqlite3.connect(r"C:\Users\saksham\Desktop\database.lastdb.db")
    c = db.cursor()
    #c.execute("create table adata(food_item,price)")
    c.execute("insert into adata(food_item,price) values('onion pizza',99)")
    c.execute("insert into adata(food_item,price) values('paneer pizza',110)")
    c.execute("insert into adata(food_item,price) values('capsicum pizza',80)")
    c.execute("insert into adata(food_item,price) values('tomato pizza',90)")
    c.execute("insert into adata(food_item,price) values('cheese pizza',120)")
    db.commit()
    db.close()

def home():
    pname=input("enter name")
    food=input("enter food item")
    quant=input("enter quantity")
    db = sqlite3.connect(r"C:\Users\saksham\Desktop\database.lastdb.db")
    c = db.cursor()
    c.execute("create table ufood(person_name,food_item,quantity)")
    c.execute("insert into ufood(person_name,food_item,quantity) values(pname,food,quant)")
    c.execute("select price from adata where food_item==food")
    d=c.fetchall()
    print("you have to pay",d,"rs at the time of delivery using cash.")
    print("you want to confirm(y/n)?")
    ch=input()
    if(ch=='y'):
        print("your order is successfully placed")
    else:
        print("sorry,try again")
    db.commit()
    db.close()


def sign_up():
    uname1=input("enter username")
    upass1=input("set your password")
    phoneno1=int(input("enter phone no."))
    db = sqlite3.connect(r"C:\Users\saksham\Desktop\database.lastdb.db")
    c = db.cursor()
    #c.execute("create table sign_up2(uname,upass,phoneno)")
    c.execute("insert into sign_up2 values(?,?,?)",(uname1,upass1,phoneno1))
    db.commit()
    db.close()



def sign_in():
    uname1=input("enter username")
    upass1=input("set your password")
    db = sqlite3.connect(r"C:\Users\saksham\Desktop\database.lastdb.db")
    c = db.cursor()
    c.execute("select upass from sign_up2 where uname=?",(uname1,))
    d=c.fetchall()
    for i in d:
        print(i)
    if(d==upass1):
        print("you are Welcome..")
    else:
        print("wrong password")
    db.commit()
    db.close()




admin1()
print("Menu")
print("1. signup")
print("2. signin")
print("3. home")
choice=input("enter your choice")
if choice=='1':
    sign_up()
elif choice=='2':
    sign_in()
elif choice=='3':
    home()
else:
    print("Invalid choice")


s