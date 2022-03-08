def cal():
    add = "+"
    sub = "-"
    mul = "*"
    div = "/"
    print('Enter the your choice for the calculation \n')
    a = int(input('Enter the first number : '))
    b = int(input('Enter the second number : '))
    c = input('Enter the your operation : ')

    if a==56 and b==9 and c=='add':
        print(77)

    elif a==56 and b==4 and c=='div':
        print(4)
    
    elif a==45 and b==3 and c=='mul':
        print(555)

    elif c=='add':
        print(a+b)
    
    elif c=='mul':
        print(a*b)

    elif c=='div':
        print(a/b)

    else:
        print(a-b)

cal()