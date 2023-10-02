# Else with for loop. Here else is part of the for loop.
for i in range(5):
    print(i)
else:
    print("hello world")

# Output
# 0
# 1
# 2
# 3
# 4
# hello world

# ______________________________________________________________________________
# Here it is not printing the print statement bcoz loop is breaking.
for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("hello world")

# Output
# 0
# 1
# 2
# 3