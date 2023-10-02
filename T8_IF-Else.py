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


#_____________________________________________________________________________

if num<0:
    print("Number is negative")
elif num>0:
    if num>0 and num<=10:
        print("Number is between 0-10")
    elif num>10 and num<=20:
        print("Number is between 10-20")
    elif num>20 and num<=30:
        print("Number is between 20-30")
    elif num>30 and num<=40:
        print("Number is between 30-40")
    else:
        print("Number is greater than 40")

else:
    print("Number is zero")

#_____________________________________________________________________________

num1= int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
op = input("Enter the operation: + - * /: ")

if op=="+":
    print(num1+num2)

elif op=="-":
    print(num1-num2)

elif op=="*":
    print(num1*num2)

else:
    print(num1/num2)

# ________________________________________________________________

import time

a = int(time.strftime('%H'))


if a<12:
    print("Good morning")

elif a>=12 and a<=16:
    print("Good afternoon")

else:
    print("Good evening")

