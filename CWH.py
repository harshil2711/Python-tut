"""
->>># 1.Make a dictionary that contains words with meaning
dict = {"difficult":"hard","immutable":"tuple","mutable":"list","workout":"body"}

n = input("What you are looking for : ")

try:
    print(dict[n])
except Exception as e:
    print('Uff....This is not available in our dictionary')

__________________________________________________________________________________________________

->>>#check the age for driving vehicle

def licence():
    age = int(input("enter your age :"))
    if age>70 or age<7:
        print("enter the age again")
        licence()
    elif age>18:
        print("u can drive")
    elif age==18:
        print("give test first")
    else:
        print("you cant drive")
licence()
__________________________________________________________________________________________________

->>># Faulty calculator

def calculator():

    choice_1 = int(input("enter first choice :"))
    choice_2 = int(input("enter second choice :"))
    operator = input("enter operator :")

    if choice_1==45 and choice_2==3 and operator=='*':
        print(555)
    elif choice_1==56 and choice_2==9 and operator=='+':
        print(77)
    elif choice_1==56 and choice_2==6 and operator=="/":
        print(4)
    elif operator=="+":
        print(choice_2+choice_1)
    elif operator=="-":
        print(choice_1-choice_2)
    elif operator=="*":
        print(choice_1*choice_2)
    else:
        print(choice_1/choice_2)

calculator()

print("continue or exit....")

yes=input("press y for continue and N for exit :")

if yes=="y" or yes=="Y":
    calculator()
elif yes=='n' or yes=="N":
    exit()
__________________________________________________________________________________________________

->>># print only integers from list

a = ['hari','har','harshil',"harkkk",25,66,88,1,3,5]
for i in a:
    if  type(i)==int and i>6:
        print(i)
__________________________________________________________________________________________________

->>> #candy shop

av=5
x=int(input("wnt"))
i=1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("candy")
    i=i+1
__________________________________________________________________________________________________

->> #Number Guessing Game
def game():
    n=18
    i = 1   
    print('You have total 5 chances to win this game..')
    while True:
        if i==6:
            print('Game over....')
            break
        print()    
        m = int(input('Enter the number : '))
        if m < n:
            print()
            print('Enter the greater number') 
        
        elif m > n:
            print()
            print("Enter the lesser number")

        else:
            print('Hurray......you won')
            print(f"You took total chances : {i}")   
            break
            
        print(f'Total remaining chances : {5-i}') 
        i=i+1
        
    print()
    play = input('Do you want continue y or n:\n')
    if play=="y":
        game()

    if play=='n':
        exit()

game()
__________________________________________________________________________________________________
# Block requirement solution

def requirement(filesize):
    block_size = 4096
    
    full_block = filesize // block_size

    remainder = filesize % block_size

    if remainder > 0:
        return (full_block * block_size)+block_size

    return full_block * block_size


print(requirement(1)) #4096
print(requirement(11111)) #4096
print(requirement(4096)) #4096
print(requirement(4097)) #4096
__________________________________________________________________________________________________
==> Return Fullname

def f1(firstname,lastname):
    if firstname=='' and lastname=='':
        return ""
    elif firstname=='' and lastname==lastname:
        return "Name: " + lastname
    elif firstname==firstname and lastname=='':
        return "Name: " + firstname    
    else:
        return "Name: " + firstname + ", " + lastname

print(f1('','Michel'))
print(f1('Anna',''))
print(f1('',''))
print(f1('illy' ,'bell'))

# Name: Michel
# Name: Anna

# Name: illy, bell
____________________________________________________________________________________________
==> Return color code

# def color_translator(color):

# 	if color == "red":
# 		hex_color = "#ff0000"
# 	elif color == "green":
# 		hex_color = "#00ff00"
# 	elif color == "blue":
# 		hex_color = "#0000ff"
# 	else:
# 		hex_color = "unknown"
# 	return hex_color

# print(color_translator("blue")) # Should be #0000ff
# print(color_translator("yellow")) # Should be unknown
# print(color_translator("red")) # Should be #ff0000
# print(color_translator("black")) # Should be unknown
# print(color_translator("green")) # Should be #00ff00
# print(color_translator("")) # Should be unknown
_______________________________________________________________________________________________
# =>>Sum of all divisor of the number

# def sum_divisors(n):
#   a=1
#   sum = 0
#   while a<n:
#       if n%a==0:  
#           sum=sum+a
#       a=a+1
#   return sum

# print(sum_divisors(10))

# ==>Method No two
# def f1(n):
#     a=1
#     b=[]
#     while a<n:
#         if n%a==0:
#             b.append(a)
#         a=a+1
#     return sum(b)

# print(f1(10))

#Prime numbers in a range
for j in range(11,20):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print(j)
    
# Output
# 11
# 13
# 17
# 19

=> Number is prime or not
n = int(input('number: '))
for i in range(2,n):
    if n%i==0:
        print('Not prime')
        break

else:
    print('prime')

# Output
# number: 50
# Not prime
"""
# Stone paper scissor game

import random

while True:

    a = ["rock" , "paper" , "scissor"]

    computer = random.choice(a)
    print()
    user = input("Enter your input : ")

    if user != "r" and user != "s" and user != "p":
        raise ValueError("invalid input error")

    if computer == 'rock' and user == 'p':
        print("You win")
        print("Computer input is 'rock' and yours is 'paper' ")

    elif computer == 'rock' and user == 's':
        print("Computer win")
        print("Computer input is 'rock' and yours is 'scissor' ")


    elif computer == 'paper' and user == 'r':
        print("Computer win")
        print("Computer input is 'paper' and yours is 'rock' ")


    elif computer == 'paper' and user == 's':
        print("You win")
        print("Computer input is 'paper' and yours is 'scissor' ")


    elif computer == 'scissor' and user == 'r':
        print("You win")
        print("Computer input is 'scissor' and yours is 'rock' ")


    elif computer == 'scissor' and user == 'p':
        print("Computer win")
        print("Computer input is 'scissor' and yours is 'paper' ")


    else:
        print("draw")
        print("Computer input and yours is same ")

# __________________________________________________________________________________________
# FOR MERFGE THE PDFS

import PyPDF2

m = PyPDF2.PdfMerger()

for content in ['sample1.pdf' , 'sample2.pdf']:
    m.append(content)

m.write('newpdf.pdf')

# _________________________________________________________________
# FOR READ THE PDF

import PyPDF2

reader = PyPDF2.PdfReader('news.pdf')

print(reader.pages[1].extract_text())

# ____________________________________________________________________
# Text to voice

import pyttsx3
i = 0
li = ['tom' , 'cruise' , 'simaran']
engine = pyttsx3.init()
for i in range(len(li)):
    engine.say(f"shout out to {li[i]}")
engine.runAndWait()


# ___________________________________________________________

# Kaun banega crorepati

questions = ["How many hours are there in a day?", "The baby frog is known as?" , "Rainbow consist of how many colours?"]
answers = ["65" ,"Tadpole" , "7" ]

prize = 0
j = 0
for i in questions:
    print("Your first question is: " , i)
    ans = input("Answer of this question : ")
    if ans==answers[j]:
        print("You are right")
        prize = prize + 100
        print("Your total winning amount is : ", prize)
    else:
        print("sorry you lost !!! , Your total winning amount is : " , prize)
        quit()
    j = j+1

