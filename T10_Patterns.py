r = int(input('enter the number : '))

for i in range(1,r+1):
    print(i * ' *')

# Output: 
# enter the number : 5
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
#__________________________________________________________________________________________________________
r = int(input('enter the number : '))
i=1

while i<=r:
    print(i * ' *')
    i=i+1

# Output: 
# enter the number : 5
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
#__________________________________________________________________________________________________________
r = int(input('enter the number : '))

for i in range(1,r+1):
    print(r * (' *'))
    r = r-1

# Output:
# enter the number : 5
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *
#__________________________________________________________________________________________________________

r = int(input('enter the number : '))
i = r

while i<=r:
    print(i * ' *')
    i = i - 1
    if i<1:
        break

# Output:
# enter the number : 5
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *
#__________________________________________________________________________________________________________
r = int(input('enter the number : '))

for i in range(1 ,r+1):
    print(r * ' *')

# Output:
# enter the number : 5
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#__________________________________________________________________________________________________________
r = int(input('enter the number : '))
i = 1

while i<=r:
    print(r * ' *')
    i = i + 1

# Output:
# enter the number : 5
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#__________________________________________________________________________________________________________
n = int(input('Enter the rows you want : '))
j = int(input('Enter the stars you want : '))
for i in range(n):
    print(j * "* ")

# Output:
# Enter the rows you want : 3
# Enter the stars you want : 8
# * * * * * * * * 
# * * * * * * * * 
# * * * * * * * * 
# _______________________________________________________________________________________________________
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print() 

# Output  
# A 
# B B 
# C C C
# D D D D
# E E E E E
# _______________________________________________________________________________________________________
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print() 

# Output
# A
# A B
# A B C
# A B C D
# A B C D E
# _______________________________________________________________________________________________________

