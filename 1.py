""""

print("\"Twinle Twinkle', How i wonder what you are\"")

print("\"hello\",\"How are you?\",sep= \" ---\"")

print("a string  that you \"don`t\" have to escape \n This \n is a ....multi line \n heredoc string ------> example ")

print("(X+Y)*(X+Y).Ex: x= \n 4,y=3")


print("\"bhargav\"")





a= "hello world"

print(len(a))


a= "w3school"
print(a[0:4])

a= "w3"
print(a+a)

a= 'abc'
b= 'xyz;'
c = b[0:2]
d=  a[0:2]
print(c+a[2])
print(d+b[2])


a= "abc"
b= "ing"
print(a+b)

a= "string"
b= "ly"
print(a+b)

a= input("enter your name")
print(a[::-1])


a= input("enter radius")
b= 3.14
print(float(b)*int(a)*int(a))

a=input("enter your name")
print(a[::-1])

a= input("enter the radius")
b= 0.75
c= 3.14
print(float(b)*float(c)*float(a)*float(a)*float(a))


a= input("enter radius")
b= 3.14
print(float(b)*int(a)*int(a))

a= input("enter the number")
print(int(a)+int(a)*int(a)+int(a)*int(a)*int(a)*int(a))

a=int(input("enter the number"))
b=a%2
if b>0:
    print("Number is odd")
else:
    print("Number is even")

a=int(input("enter the number"))
b=a%2
if b==0:
    print("Number is odd")
else:
    print("Number is even")

a=input("enter the alphabet")
b='a','e','i','o','u'
for x in b:
    if a in b:
        print("it is vowel")
        break
    else:
        print("it is constant")
        break



a=input("enter the height")
b=input("enter the base")
print(int(a)*int(b)/2)

a=10
b=-10
c=20
print(a+b)
print(a+b+c)

a=10
b=10
if a==b:
    print("true")

for x in range(1,7):
    if x%3==0 or x%6==0:
        continue
    print(x)

i=0
while i<=5:
    i=i+1
    if i%3==0 or i%6==0:
        continue
    print(i)

a=["red","green","white","black"]
print(a[0],a[3])

a=["red","green","white","black"]
print(len(a))

a=["audi","mercy","bmw","honda"]
if "audi" in a:
    print("value is not available")
else:
    print("value is not available")

y=1
a=[1,2,3,9,7]
for x in a:
    y=y*x
print(y)

a= int(input("enter the vlaue"))
b=(a*(a+1))/2
print(b)

a=["red","black","grey","yellow"]
print(a[0],a[3])

a=[1,3,5,7]
if -1 in a:
    print("true")
else:
    print("false")

numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,  815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527 ]
for x in numbers:
    if x == 237:
        break
    if x%2==0:
        print(x)

5.  a=[1,3,7,-6,-7,-2,55]
    for x in a:
        if x>=0:
            print(x)

5.  i=0
    a=[1,3,5,6,-9,-7]
    while i<=len(a):
        if a[i]>=0:
            print(a[i])
        i=i+1

7.  print(float(2))

8.  a=[1,3,69,7,8,2]
    print(len(a))

9.  a=[1,3,5,6,3]
    print(sum(a))

10. y=1
    a=[6,3,4,6,3]
    for x in a:
        y=y*x
    print(y)

11. a=[20,30,60,100,800]
    print("max value is",max(a))

12  a=[20,30,60,100,800]
    print("max value is",min(a))


13. a=["abc","1221","aba","xyz"]
    for x in a:
        if len(x)>=3 and x[0]==x[-1]:
          print(x)

15. a=["maruti","honda","audi","kia","suzuki","maruti","kia","maruti"]
    print(list(set(a)))

16. a=[1,3,6,36,9,6]
    if len(a)==0:
        print("list is empty")
    else:
        print("list is not empty")

17. a=[1,2,6,8,9,4,5,8,0]
    b=a.copy()
    print(b)

20. a=[1,69,3,85,96,78,4,26,35,15]
    for x in a:
        if x%2!=0:
        print(x)

21. import random
    l=list(range(5))
    random.shuffle(l)
    print(l)

22. import itertools
    print(list(itertools.permutations("12697",3)))

23. a=[1,3,6,9,4,5,10,36,96,78,45]
    b=[1,3,6,9,5,10,78,45]
    c=[]
    for x in a:
        if x not in b:
            c.append(x)
    print(c)

24. b = [1, 3, 6, 9, 5, 10, 78, 45]
    print(b[1])

25. a=['h','a','r','s','h','i','l']
    b=''.join(a)
    print(b)

26. a = [1, 3, 6, 9, 5, 10, 78, 45]
    print(a.index(78))

27. a=[1,3,5,7,9]
    b=[2,4,6,8,10]
    for x in b:
        a.append(x)
    print(a)

27. a=[1,3,5,7,9]
    b=[2,4,6,8,10]
    c=a+b
    print(c)

28. a=[1,59,36,966,96,66,45]
    a.sort()
    print("second largest number is :",a[-2])

29. list2 =[1, 2, 1, 1, 3, 4, 3, 3, 5]
    print(list(set(list2)))

31. a=["maruti","honda","audi","mercy","maruti"]
    b=[x[1] for x in a]
    print(b)

33. a=[13,66,99,42,53,335]
    b=[2,366,352,36,25,46]
    c=a+b
    print(c)

34. a="harshil"
    print(list(a))

35. a=[1, 3, 5, 7, 9, 10]
    b=[2, 4, 6, 8]
    print(b+a[-1:])

36. a = {"zname": "pradip", "xname": "Rajput", "yname1": "karan"}
    b=list(a.items())
    b.sort()
    print(b)
    b.sort(reverse=True)
    print(b)

37. a={0:"har",1:"harshil",3:"shukla"}
    a[4]="abc"
    print(a)

38. dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    dic4={}
    dic4.update(dic1)
    dic4.update(dic2)
    dic4.update(dic3)
    print(dic4)

40. a=dict()
    for x in range(0,15):
        a[x]=x*x
    print(a)

41. dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic1.update()
    print(dic1)

42. dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    dic4={}
    dic4.update(dic1)
    dic4.update(dic2)
    dic4.update(dic3)
    print(dic4)

43. a=()
    print(type(a))

44. a=("harshil",3.5,True,36)
    print(a)

47. a=(1,3,9,6,89,45)
    b=list(a)
    b.append(70)
    print(tuple(b))

48. a=("h","a","r")
    b="".join(a)
    print(b)

50. a=(1,3,6,3,99,99,69,3)
    print(a.count(99))

51. a=(1,3,6,3,99,99,69,3)
    if 100 in a:
        print("yes")
    else:
        print("no")

52. a={}
    print(a)

54. a={1,6,9,3,7,9}
    a.add(10)
    print(a)

55. a = {1, 6, 9, 3, 7, 9}
    a.remove(9)
    print(a)

57. a = {1, 6, 9, 3, 7, 9}
    b= {2,4,5,6,8,10}
    c=a|b
    print(c)

58. a = {1, 6, 9, 3, 7}
    b = {1,6,9}
    for x in a:
        if x not in b:
            print(x)

59. a={1,36,8,9,3,56,69}
    b={2,36,96,58,56,3,12,14}
    c=a^b
    print(c)


60.a={1, 6, 9, 3, 7}
    b={1,6,9}
    print(a.issuperset(b))
    print(b.issubset(a))

61. a = {1, 6, 9, 3, 7}
    b = a.copy()
    print(b)

62. a = {1, 6, 9, 3, 7}
    a.clear()
    print(a)

math exercises

1,2. from math import *
     a=10
     print(radians(a))
     print(degrees(a))

3.  a=int(input("enter the height"))
    b=int(input("enter the base"))
    c=a*b
    print(c)

4.  h=int(input("enter the height"))
    pi=3.14
    r=int(input("enter the radius"))
    v=h*pi*r*r
    a=2*pi*r*(r+h)
    print(v)
    print(a)

5.  r=int(input("enter the radius"))
    pi=3.14
    v=4/3*pi*r
    a=4*pi*r*r
    print(v)
    print(a)

7.  from  math import *
    r=int(input("enter the radius"))
    a=int(input("enter the angle"))
    b=radians(a)
    c=1/2*r*r*b
    print(c)

-> Function exercise
1. def max(a,b,c):
        if a>b and a>c:
            print(a)
        elif b>a and b>c:
            print(b)
        else:
            print(c)
    max(20,300,50)

2.  def sum(*args):
        y=0
        for x in args:
            y=y+x
        print(y)
    sum(8,2,3,0,7)

3.  def mul(*args):
        y=1
        for x in args:
            y=y*x
        print(y)
    mul(8,2,3,-1,7)

4.  def reverse(x):
        return x[::-1]
    print(reverse("1234abcd"))

5.  x=input("enter the number")
    def factorial(x):
        if x==1:
            return 1
        else:
            return x*factorial(x-1)
    print(factorial(5))

5.  def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
    n=int(input("number"))
    c=fact(n)
    print(c)

5.  i=1
    a=int(input("enter the number"))
    for x in range(a,0,-1):
        i=i*x
    print(i)

6.  def ran(x):
    if x in  range(2,9) :
        print("yes")
    else:
        print("no")
    ran(10)

7.  def unique(*args):
    b=[]
    for x in args:
        if x not in b:
            b.append(x)
    print(b)
    unique(1, 3, 6, 5, 3, 1, 5, 9, 23, 6, 23, 6, 1, 9)

8.  def even(*args):
        b=[]
        for x in args:
            if x%2==0:
                b.append(x)
        print(b)
    even(1,2,3,4,5,6,7,8,9,2,6,4)

8.  a=[1,3,6,85,95,55,63,1,254,3,64,78,96]
    b=list(filter(lambda n:n%2==0,a))
    print(b)
`
9.  def square():
    a=[]
    for x in range(1,31):
        c=x*x
        a.append(c)
    print(a)
    square()

9.  a=[]
    for x in range(1,31):
        a.append(x)
    print(a)
    b=list(map(lambda j:j**2,a))
    print(b)

12. subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    subject_marks.sort(key=lambda x:x[1])
    print(subject_marks)

12. subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    b=sorted(subject_marks,key=lambda x:x[1])
    print(b)

13. models = [{'make':'Nokia', 'model':216, 'color':'Red'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
    b=sorted(models,key=lambda x:x["color"])
    print(b)

13. models = [{'make':'Nokia', 'model':216, 'color':'Red'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
    models.sort(key=lambda x:x["color"])
    print(models)

14. a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b=list(filter(lambda x:x%2==0,a))
    print("even numbers from the lsit are:")
    print(b)
    c=list(filter(lambda x:x%2!=0,a))
    print("odd numbers from the lsit are:")
    print(c)

15. def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for x in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
    n=int(input("enter the number"))
    fib(n)

15. def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)
for n in range(1, 11):
    print(n, ":", fib(n))


-> OOPS
3.
x=int(input("enter the x :"))
n=int(input('enter the n :'))
class pov:
    def pow(self,x,n):
        if n==0:
            return 1
        elif n==1:
            return x
        elif n>1:
            return x*pow(x,n-1)
c1=pov()
print(c1.pow(x,n))

5.
class abc:
    def __init__(self,string):
        self.input=string

    def reverse(self):
        a=list(self.input)
        b=reversed(a)
        c="".join(b)
        print(c)
c1=abc("my name is harshil shukla")
c1.reverse()

6.
r=int(input("enter the radius :"))
from numpy import *
class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius*pi*self.radius
    def perimeter(self):
        return 2*pi*r
obj1=circle(r)
print(obj1.area())
print(obj1.perimeter())

-> File i/o
1.  f1=open("text1","r")
    print(f1.read())

2.  f1=open("text1","r")
    f2=f1.readlines()
    print(f2[3])

3.  f1=open("text1","r")
    print(f1.readline(10))

"""
a=['har',"hari"]
print(a[0])