def check_password():
    x=1
    n=3
    while x <= 4:
        u = input('enter your username')
        p = input('enter your password')
        if p == 'charlie':
                print('signin successfully')
                return 1
        else:
            if n!=0:
                print('you have entered wrong password..you have',n,'chances left....try again.')
                x+=1
                n-=1
            else:
                print('You are Blocked')
                return 0
a=check_password()
if a==1:

else:
    print('you dont have access here')

