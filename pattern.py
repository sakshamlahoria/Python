print("how many rows you want to print")
a=int(input())
print("Type 1 or 0")
b=int(input())
c=bool(b)
if c==True:

    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif c== False:
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()