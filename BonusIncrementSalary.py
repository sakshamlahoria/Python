d={}
user=int(input('enter the no. of employees'))
for i in range(user):
    a=input('enter the name of the employees')
    b=int(input('enter the salary of the employees'))
    d[a]=b
for x,y in d.items():
    if y>20000:
        d[x]=y+2500
    else:
        d[x]=y+5000
