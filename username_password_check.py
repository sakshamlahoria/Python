a=input('enter your username')
b=input('enter your paassword')
for x in range(6):
    if x < 4:
        c=input('enter your username')
       
        if a == c:
            for y in range(6):
                if y < 4:
                    d=input('enter your password')
                    
                    if d == b:
                        print('signin successfully')
                        break
                    else:
                        print('wrong password')
                elif y == 4:
                    print('this is your last attempt')
                    e=input('enter your password')
                    if e == b:
                        print('signin successfully')
                        break
                    else :
                        print('your account is blocked')
        else:
            print('invalid username')
    elif x == 4:
        q=input('enter your username')
        break
        if q == a:
            for m in range(6):
                if m < 4:
                    p=input('enter your username')
                    break
                    if p == a:
                        print('signin successfully')
                        break
                    else:
                        print('wrong username')
                elif m == 4:
                    print('this is your last attempt')
                    g=input('enter your username')
                    break
                    if g == a:
                        print('signin succesfully')
                        break
                    else:
                        print('your account is blocked')
                        break
        else:
            print('account blocked')
    else:
        print('account blocked')
        break
    break
        
        
                
