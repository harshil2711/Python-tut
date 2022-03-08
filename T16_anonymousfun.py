# Lambda function

from ast import Lambda
from smtplib import LMTP


x = lambda a,b : a+b
print(x(3,5))

# Output
# 8

# _________________________________________________________________________________________

a = [[2,5], [23,2] , [44,59] , [0,3]]
a.sort(key= lambda x:x[1])
print(a)

# Output
# [[23, 2], [0, 3], [2, 5], [44, 59]]