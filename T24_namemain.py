# If you import 1 file in 2nd file then run second file , It will execute the all the functions of the file1.
# To overcome this issue , Use if __name__ == '__main__': and put the executable function in this body in file 1.

# File 1 :

def welcome(name):
    print(f"you are welcome{name}")


if __name__ == '__main__':

    welcome("haarry")

# ___________________________________________________________________________________

# File 2 :

import file1

file1.welcome("kajal")

# Now it will execute only KAJAL file when you run this file 2.