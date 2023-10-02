"""
Ordered, Indexed, Unchangeable, Duplicate value accept

"""
tup = (1,5,6)
print(type(tup))

# Output
# <class 'tuple'>

# ____________________________________________________________

tup = (1)
print(type(tup))

# Output
# <class 'int'>

# ____________________________________________________________
tup = (1,)
print(type(tup))

# Output
# <class 'tuple'>
# _______________________________________________________________________

a = ('apple' , 'orange' ,'grapes' , 'banana', 'grapes')

print(a.index('grapes'))

# Output
# 2
# _____________________________________________________________________
a = ('apple' , 'orange' ,'grapes' , 'banana', 'grapes')

print(a.count('grapes'))

# Output
# 2

# _____________________________________________________________________

a = ('apple' , 'orange' ,'grapes' , 'banana', 'grapes')

print(len(a))

# Output
# 5