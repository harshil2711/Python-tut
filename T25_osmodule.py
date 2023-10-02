import os

for i in range(1,101):
    os.mkdir(f"T_{i}")

# Output
# It will create 100 folders.

# ____________________________________________________________________________________________

import os

for i in range(1,101):
    os.rename(f"File_{i}", f"Folder_{i}")


# Output
# To rename the file


# ________________________________________________________________________________________________

import os

folders = os.listdir('one')

for i in folders:
    print(i)


#Output
# To list all the dictonary

# ___________________________________________________________________________________________________

import os

folder = os.listdir('one')

for i in folder:
    print(os.listdir(f"one/{i}"))


#Output
# To list all subdirectory in the main directory.