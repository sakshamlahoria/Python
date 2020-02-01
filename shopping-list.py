shopping_list=[]
print('what to take with you')
print('enter DONE to stop the process')
while 3:
    items=input('enter the items')
    if items=='DONE':
        break
    shopping_list.append(items)
    print('your list:')
    for item in shopping_list:
        print(item)
