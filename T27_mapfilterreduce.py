# Map , You can use with list , tuple , set.

l = [1,2,3,4,5,6,7]

newl = set(map(lambda x : x * x * x , l))

print(newl)


# ________________________Filter________________________________
# You can use with list , tuple , set

newlist = list(filter(lambda x:x>4 , l))

print(newlist)


# ________________________Reduce________________________________
# No need to use with tuple , list or set

from functools import reduce

filerlist = reduce(lambda x,y : x + y , l)

print(filerlist)


