i = 0
while i<=3:
    print(i)
    i=i+1

# Output
# 0
# 1
# 2
# 3

# ______________________________________________________________________________________________
I = int(input("Enter ther I : "))

while I<12:
    print(I)
    I = I + 1

# Output
# Enter ther I : 2
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11

# _________________________________________________________________________
i = 5

while i > 0:
    print(i)
    i = i - 1

# Output
# 5
# 4
# 3
# 2
# 1

# _________________________________________________________________________

i = 1
while i<=5:
    print("Hello",end=" ")
    j=1
    while j<=4:
        print("world",end=" ")
        j=j+1
    i=i+1
    print()


# Output:
# Hello world world world world
# Hello world world world world
# Hello world world world world
# Hello world world world world
# Hello world world world world


# _______________________________________________________________________
i = 1

user = int(input("how many you want : "))

av = 5

while i<=user:
    if i>av:
        print("sorry")
        break
    print("candies")
    i=i+1
