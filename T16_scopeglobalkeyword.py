# Local variable . It is only used by the function it self.
# You can not use 'l' outside the function.

def myfunc(n):
    l = 5  #Here 5 i local variable boz it is inside the function.
    print(l)
    print(n , 'Today is wednesday')

myfunc('Hello')

# Output
# 5
# Hello Today is wednesday

# _______________________________________________________________________________________________
# Global Variable. You can use it inside or outside the function.

g = 10  #It is global variable.

def myfunct1(n):
    print(g)
    print(n,'Tomorrow is sunday')

myfunct1("hi")
print(g)

# Output
# 10
# hi Tomorrow is sunday
# 10

# _______________________________________________________________________________________________
"""
Here if global variable and local variable has a same name then it will find for a local variable
and if it not present then it will go for a global variable.
here it is printing 20 bcoz local variable is present.
"""

m = 15

def myfunct2():
    m = 20
    print('python', m)

myfunct2()

#Output
# python 20

# _______________________________________________________________________________________________
# 'Global' keyword
# Global keyword is used for the change the value of glabal variable

t = 10

def myfunct3():
    global t
    t = 30
    print('global variable is : ' , t)

myfunct3()

#Output
# global variable is :  30