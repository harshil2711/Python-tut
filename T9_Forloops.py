l = ['harry','marry','carry','sharry']
for x in l:
    print(x)

# Output:
# harry
# marry
# carry
# sharry
# ____________________________________________________________________________________________________
l = [['harry',1],['marry',5],['carry',2],['sharry',2]]

for i in l:
    print(i)

# Output:
# ['harry', 1]
# ['marry', 5]
# ['carry', 2]
# ['sharry', 2] 
# ____________________________________________________________________________________________________
l = [['harry',1],['marry',5],['carry',2],['sharry',2]]

for i,j in l:
    print(i,"has",j,"car")

# Output:
# harry has 1 car
# marry has 5 car
# carry has 2 car
# sharry has 2 car
# ____________________________________________________________________________________________________
l = [['harry',1],['marry',5],['carry',2],['sharry',2]]
m = dict(l)

for i,j in m.items():
    print(i,'has',j,'cars')

# Output:
# harry has 1 cars
# marry has 5 cars
# carry has 2 cars
# sharry has 2 cars
# ____________________________________________________________________________________________________
l = [['harry',1],['marry',5],['carry',2],['sharry',2]]
m = dict(l)

for i in m:
    print(i)

# Output:
# harry
# marry
# carry
# sharry

# _______________________________________________________________________________________________________
l = [2,1,9,'harry',False,66,'carry',5,36,'mukesh'] #print the number greater than 6 in the list.

for i in l:
    if str(i).isnumeric() and i>6:
        print(i)

# Output: 
# 9
# 66
# 36

# _______________________________________________________________________________________________________
for i in range(10):
    print(x)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# _______________________________________________________________________________________________________
for i in range(5):
    print('To day is night',i)

# Output: 
# To day is night 0
# To day is night 1
# To day is night 2
# To day is night 3
# To day is night 4

# _______________________________________________________________________________________________________
for i in range(10,15):
    print(i)

# Output: 
# 10
# 11
# 12
# 13
# 14
# _______________________________________________________________________________________________________
for i in range(11,20,2):
    print(i)

# Output:
# 11
# 13
# 15
# 17
# 19
# _______________________________________________________________________________________________________

c = int(input('How many Candy you want : '))
av = 2

for i in range(1,c+1):
    if i>av:
        print('sorry we are out of stock...')
        break
    print('candy')

# Output:
# How many Candy you want : 5
# candy
# candy
# sorry we are out of stock...

#_____________________________________________________________________________________________


c = int(input('How many Candy you want : '))
av = 5
i=1
while i<=c:
    print('candy')
    i=i+1
    if i>av:
        print('sorry we are out of stock')
        break
    
# Output:
# How many Candy you want : 9
# candy
# candy
# candy
# candy
# candy
# sorry we are out of stock

