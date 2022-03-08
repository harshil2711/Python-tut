"""
-> Language :
        -> Markup language: HTML,XML
                ->Tag , attribute, aatribute value.
        -> Styling tool : CSS
        -> Scripting Language :
             -> Client side Scripting Language
                -> it run on client machine
                -> ex. JS
                -> it is less secure
             -> server side Scripting Language
                -> it run server machine
                -> it more secure
                -> ex : PHP, Python, ASP

        -> Programming Lnagugae :
                -> third party tool : complier
                -> java, C, C++ :

-> Python :
        -> Download & install :

version :
     ->  3(major).8(minor).5(patch)


->
    print("Hello World")

--> Variable :
    -> temporarry memory staorage.
    ->
        abc = "Hello Wolrd, Today is beautiful day"
        print(abc)

-> escape sequense:
\" -> "
\' -> '
\\ -> \
\n -> new line
\t - > tab


print("\"Twinkle, twinkle’, How I wonder what you are\"")

-> Data Type :
        -> Number :
            -> int:
            -> float :
            -> complex :

        -> string :
            -> "hello World"


        -> Boolean :
                -> True :
                -> False :

        -> collection :
                -> array :
                -> list :
                -> tuple :
                -> set :
                -> dictionary :

        -> object :
                -> real time entity for class.


->
    f1 = "hello World"
    print(type(f1))

->
    f1 = 123j + 5
    print(type(f1))

->
    f1 = False
    print(type(f1))

-> Casting :
        -> Int :
            a = 150
            b = "250"

            print(a+int(b))

->
    a = 150
    b = "250"
    print(str(a)+b)

->
    a = 150.90
    b = 250
    print(int(a+b))

->
    a = "150.90"
    b = 250
    print(float(a)+b)

->
    a = "150.90"
    b = 250
    print(int(float(a)+b))

->
    a = "Hello World, Today is beautiful day"
    print(a[1])

->
    a = "Hello World, Today is beautiful day"
    print(a[5:11])

->
    a = "                         Hello World, Today is beautiful day                          "
    print(a.strip())

->
    a = "Hello World, Today is beautiful day"
    print(len(a))

->
    a = "Hello World, Today is beautiful day"
    print(a.upper())
->
    a = "Hello World, Today is beautiful day"
    print(a.lower())

->
    a = "Hello World, Today is beautiful day"
    print(a.replace("is", "DAY"))

->
a = "Hello World, Today is beautiful day"
print(a.split(' '))

->
    a = "Hello World, Today is beautiful day"
    print(a.split('i'))

->
    a = input("Please Enter Your Name")
    print(a)

->
    a = input("Please Enter Your Number")
    print(int(a)+100)

->
    a = input("Please Enter Your Number")
    print(type(a))

->  use of end=''
    print('my name is harshil shukla', end=' ')
    print('i live in ahmedabad')
    output= my name is harshil shukla i live in ahmedabad

-> Operator :
    ->
        Arithmatic Operators(+,-,*,/,**,//,%):

    ->
        a = 2
        b = 5
        print(a**b)

    ->
        a = 20
        b = 5
        print(a/b)

    ->
        a = 21
        b = 5
        print(a/b)

    ->
        a = 21
        b = 5
        print(a%b)

    -> Bitwise Operator :
       ->

11 10 -> 1011 1010


And Operation :

-> 10 -> 1010
-> 11 -> 1011
---------------
         1010 -> 10

->
    a = 10
    b = 11
    print(a&b)

->
    a = 1010
    b = 1111
    --------
        1111

->
    a = 15
    b = 10
    print(a|b)

-> a = 15 -> 1111
-> b = 10 -> 1010
-------------------
             0101

->
a = 15
b = 10
print(a^b)

10 -> 1010

-> 0010 1000
-> 0001

->
    a = 10
    b = 2
    print(10>>3)

-> Assignment Operator (=, ):

    -> a = a+10
    -> b = b+20

->
    b = 10
    b += 10
    print(b)
->
    a = 10
    b = 20
    if a>b:
        print("My a value is less than b value")
        print("Hello World")
    else:
        print("My a value is greter than b value")
        print("hello World")

->
    a = 20
    b = 20
    if a>b:
        print("My a value is less than b value")
    elif a==b:
        print("My a value is equal to b value")
    else:
        print("My a value is greter than b value")

->
a = 20
b = 20

if a>b:
    print("My a value is less than b value")
elif a==b:
    print("My a value is equal to b value")
elif a==b:
    print("My a value is equal to b value")
elif a==b:
    print("My a value is equal to b value")
else:
    print("My a value is greter than b value")

->
a = 10
b = 20

if a>=b:
    if a>b:
        print("My a value greter than b value")
    else:
        print("My a value is equal to b value")
else:
    print("My a value is less than b value")

->
    a = 30.2
    b = 20

    if a>=b: print("my a value is greter than or equal to  b value")

->
    a = 20
    b = 20

    if a>=b and a>b:
        print("My both condition is correct")
    else:
        print("my both or a single condition is wrong")

->
    a = 10
    b = 20

    if a>=b or a>b:
        print("My both or a single condition is correct")
    else:
        print("my both  condition is wrong")

-> Looping:
a = 0
while a<=10:
    print("Hello World, Today is beautiful day "+str(a))
    a+=1

-> break :

a = 0
while a<=10:
    if a == 5:
        break
    print("Hello World, Today is beautiful day "+str(a))
    a+=1

-> continue :
    a = 0
while a<=10:
    a += 1
    if a == 5:
        continue
    print("Hello World, Today is beautiful day "+str(a))

-> For :
for x in range(10):
    print("Hello World, Today is beautiful day "+str(x))

->
for x in range(11,20):
    print("Hello World, Today is beautiful day "+str(x))

->
for x in range(1,100,5):
    print("Hello World, Today is beautiful day "+str(x))

->
for x in range(0,100,5):
    print("Hello World, Today is beautiful day "+str(x))
else:
    print("My loop is terminated")

->
    a = int(input("Enter First value"))
    b = int(input("Enter Second Value"))

    if a == b:
        print("True")
    elif a+b == 5:
        print("True")
    elif a-b == 5 or b-a == 5:
        print("True")
    else:
        print("False")

->
    amount = int(input("Enter the amount"))
    year = int(input("Enter The year"))
    rate = int(input("Enter Rete inters"))
    inters = (amount*year*rate)/100
    print(inters)

->
    a = "Hello World, Today is beautiful day"
    for x in a:
        print(x+ " : " + str(a.count(x)))

-> Collections :
    -> List :
    -> Tuple :
    -> Set :
    -> dictionary :
    -> Array :


-> Tuple :
    ->  
    ->
-> Ex :
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    print(a)

->
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    a[0] = "Honda"
    print(a)

->
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    for x in a:
        print(x)

->
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    if "Maruti" in a:
        print("My value is available")
    else:
        print("My value is not available")

->
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    print(len(a))

->
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    del a
    print(a)

->
    a = ["maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"]
    print(tuple(a))

->
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    print(list(a))

-> set :
        -> unordered, unindexed, duplicate value not accept, changeable.
        -> curly bracket.
->
    a = {"maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"}
    print(a)

->
    a = {"maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"}
    for x in a:
        print(x)

->
    a = {"maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"}
    a.add("Honda")
    print(a)

->
    a = {"maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"}
    a.update(["Honda", "Renault", "kia"])
    print(a)

->
    a = {"maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"}
    a.clear()
    print(a)

->
    a = {"maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"}
    del a
    print(a)

->
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    print(tuple(a))

->
    a = ("maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti")
    print(set(a))

-> Dictionary:
    -> ordered, indexed(key), duplicate accept , changable
    -> curly bracket:
->
    a = {"fname":"pradip", "lname":"Rajput", "fname":"karan"}
    print(a)
->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    print(a['fname'])

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    a['fname1'] = "Karthik"
    print(a)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    for x in a:
        print(x)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    for x in a.values():
        print(x)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    for x,y in a.items():
        print(x)
        print(y)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    if "pradip" in a.values():
        print("My value is available")
    else:
        print("My value is not available")

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    print(len(a))

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    a.pop("fname")
    print(a)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    a.popitem()
    print(a)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    a['lname2'] = "Kaushik"
    print(a)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    del a
    print(a)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    a.clear()
    print(a)

->
    a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
    b = a.copy()
    print(b)

->
    from math import *
    a = 16
    print(sqrt(a))

->
    from math import *
    a = 16.25
    print(floor(a))

->
    from math import *
    a = 16.25
    print(ceil(a))

-> Array :
    -> it is also collection :

from array import *
a = array("I", [1,2,3,4,5,6,7])
print(a)

->
from array import *
a = array("I", [1,2,3,4,5,6,7])
print(a.typecode)

->
    from array import *
    a = array("I", [1,2,3,4,5,6,7])
    print(a.buffer_info())

->
    from array import *
    a = array("I", [1,2,3,4,5,6,7])
    print(type(a))

->
from array import *
a = array("I", [1,2,3,4,5,6,7])
print(a[2])

->
    from array import *
    a = array("I", [1,2,3,4,5,6,7])
    for x in a:
        print(x)

->
    from array import *
    a = array("I", [1,2,3,4,5,6,7])
    arr1 = array("I", [x*x for x in a])
    print(arr1)

->
    from array import *
    a = array("i", [1,2,-3,-4,5,6,7])
    arr1 = array("i", [x*x for x in a])
    print(arr1)

->
from array import *
array1 = array('i', [])
lengh = int(input("Enter the length"))
for x in range(lengh):
    abc = int(input("Enter the value"))
    array1.append(abc)

print(array1)

-> list comprehention :
    abc = [1,2,3,4,5,6]
    a1 = [-x*x for x in abc]
    print(a1)

->
    abc = ["maruti", "mahindra", "kia", "honda", "audi", "BMW"]
    a1 = [x[1] for x in abc]
    print(a1)

->
    abc = [1,2,3,4,5,6]
    a1 = [-x*x if x%2 == 0 else -x for x in abc ]
    print(a1)

-> Dictionary Comprehention :
    ->
        abc = {x:x**2 for x in range(1,10)}
        print(abc)

    ->
        abc = "Hello World, Today is beautiful day"
        f1 = {x:abc.count(x) for x in abc}
        print(f1)

    ->
        abc = "Hello World, Today is beautiful day"
        f1 = {x:('space' if x == " " else "character") for x in abc}
        print(f1)

-> Set Comprehention:

    abc = {k**2 for k in range(1,10)}
    print(abc)
->
    f1 = ["maruti", "mahindra", "kia", "honda", "audi", "BMW"]
    abc = {k[1] for k in f1}
    print(abc)

->
    a = 10
    b = 20
    a,b = b,a
    print("a :",a , "b :",b)

-> function way:
    ->
    def f1():
        print("Hello World, Today is a beautiful day")

    f1()
->
    def f1(fname, lname):
        print("Hello World, Today is a beautiful day by "+ fname + " " +lname)

    f1("pradip", "rajput")

->
    def f1(fname, lname="rajput"):
        print("Hello World, Today is a beautiful day by " + fname + " " + lname)

    f1("karan", "rathod")

->
def f1(fname, lname="rajput"):
    print("Hello World, Today is a beautiful day by " + fname + " " + lname)

f1("karan", "rathod")

->
def f1(fname="pradip", lname):
    print("Hello World, Today is a beautiful day by " + fname + " " + lname)

f1("karan")

->
def f1(a,b,c):
    e = a+b+c
    d = e-a
    return d

def f2(a,b,c):
    e = a+b+c
    d = e-a
    return d

d = f1(10,20,30)+f2(10,20,30)
print(d)

-> lambda :
    d = lambda a:a+10
    print(d(10))

->
    d = lambda a,b,c:a+b+c
    print(d(10,20,30))

->
def f1(*args):
    print(args)

f1("pradip","karan","kaushik","kesuri")

->
    def f1(*args):
    for x in args:
        print(x)

f1("pradip","karan","kaushik","kesuri")

->
def f1(fname, *args):
    print(fname)
    for x in args:
        print(x)

f1("pradip","karan","kaushik","kesuri")

->
    def f1(fname, lname, *args):
        print(fname)
        print(lname)
        for x in args:
            print(x)
    f1("pradip","karan","kaushik","kesuri")

->
    def f1():
        a = 10
        b = 20
        c = a+b
        return c

    print(f1())

->
    def f1(**kwargs):
    print(kwargs)

    f1(Pradip="Rajput",karan="rajput")

->
    def f1(**kwargs):
    for x in kwargs.values():
        print(x)
    f1(Pradip="Rajput",karan="rajput")

->
    a = 10
    print(f"Hello World, Today is {a}beautful day")

->

def f1(fname="karthik", **kwargs):
    print(fname)
    for x in kwargs.values():
        print(x)


f1(Pradip="Rajput", karan="rajput")

->
def f1(*args, **kwargs):
    print(args)
    print(kwargs)
f1("karthik", "karan", Pradip="Rajput", karan="rajput")

->
a = 10

def f1():
    a = 11
    print(id(a))

print(id(a))
f1()

->
a = 10
def f1():
    global a
    a = 20
    print(id(a))

f1()
print(id(a))

->
a = 10

def f1():
    a = 30
    b = globals()['a'] = 20
    print(id(b))
    print(id(a))
f1()
print(id(a))

-> Pass Statement :
for x in range(10):
    if x == 5:
        pass

    print(x)

->
def f1():
    pass

def f2():
    pass
f1()
f2()

->
a = [1,2,3,4,5,6,7,8,9]

def f1(abc):
    return abc%2 != 0
    

print(set(filter(f1, a)))

->
a = [1,2,3,4,5,6,7,8,9]

def f1(abc):
    return abc%2 != 0

print(set(filter(f1, a)))

->
a = [1,2,3,4,5,6,7,8,9]

def f1(abc):
    return abc**2

print(tuple(map(f1, a)))

->
def abc(a,b):
    if a<b:
        a,b = b,a
    return a/b


def f1(func):
    def inner(a,b):
        return func(a,b)
    return inner


div = f1(abc)
print(div(10,20))

-> Module :
    from calc import *
    print(add(10,20,30))
    print(sub(10,20))
    print(mul(20,30,10,20))

-> OOPS:
    -> What is OOPS?
        -> Methodology.
        -> Objec Oeriented Programming system.
        -> class & object.
->
    a = 10
    print(type(a))

->
    class abc:
        def f1(self):
            return "Hello World"

    obj1 = abc()
    print(obj1.f1())

-> Constructor:
    __init__()

->
    class abc:
    def __init__(self):
        print("Hello World")

    obj1 = abc()
->
    class abc:
    def __init__(self, fname, lname):
        print("Hello World from", fname, lname)

    obj1 = abc("pradip","Rajput")

-> self :
    ->
class abc:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Hello World from", fname, lname)

    def f1(self):
        print(self.fname + self.lname)

obj1 = abc("pradip","Rajput")
obj2 = abc("karan","Patel")

obj1.f1()

->
class abc:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Hello World from", fname, lname)

    def f1(self):
        print(self.fname + self.lname)

    def compare(self, other):
        if self.lname == other.lname and self.fname == other.fname:
            print("Value compared")
        else:
            print("Not Compared")

obj1 = abc("pradip","Rajput")
obj2 = abc("pradip","Rajput")
obj1.compare(obj2)

-> Type of Variable:
    -> static variable(class variable):
    -> instance variable:
            class abc:
            wheel = 4
            def __init__(self):
                self.mil = 11
                self.com = "maruti"

        f1 = abc()
        f1.mil = 12
        print(f1.mil)
        print(f1.com)
->
    class abc:
    wheel = 4
    def __init__(self):
        self.mil = 11
        self.com = "maruti"

    print(abc.mil)

-> Type of method :
    -> static Method :
        ->
        class abc:
            def __init__(self):
                self.mil = 11
                self.com = "maruti"

            def f1():
                print("Hello World, Today is a beautiful day")
        abc.f1()

    -> instance method :
        class abc:
            def __init__(self):
                self.mil = 11
                self.com = "maruti"

            def f1(self):
                print("Hello World, Today is a beautiful day")

        f2 = abc()
        f2.f1()
    -> class method:
        ->
            class abc:
                wheel = 4
                def __init__(self):
                    self.mil = 11
                    self.com = "maruti"

                @classmethod
                def f1(self):
                    print(self.wheel)

            abc.f1()

-> Inner Class :
    ->
        class f1:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.obj2 = self.laptop

    def avg(self):
        sum = self.m1 + self.m2
        return  sum

    class laptop:
        m3 = "Hello World"
        m4 = "Today is beautiful day"
        def f3():
            print("Hello John Doe")


    obj1 = f1(10,20)
    obj3 = obj1.obj2
    obj3.f3()

-> Inheritance:
    -> Single Inheritance:
    -> Multi level inheritance:
    -> Multiple Inheriance

->
class A:
    def f1(self):
        print("This is Class A Functionality")

class B(A):
    def f2(self):
        print("This is Class B Functionality")


obj1 = B()
obj1.f2()

->
class A:
    def f1(self):
        print("This is Class A Functionality")

class B(A):
    def f2(self):
        print("This is Class B Functionality")

class C(B):
    def f3(self):
        print("This is Class C functionality")

obj1 = C()
obj1.f3()

->
    class A:
        def f1(self):
            print("This is Class A Functionality")

    class B:
        def f2(self):
            print("This is Class B Functionality")

    class C(A,B):
        def f3(self):
            print("This is Class C functionality")

    obj1 = C()
    obj1.f2()

->
class A:
    def f1(self):
        print("This is Class A Functionality")

class B:
    def f2(self):
        print("This is Class B Functionality")

class C():
    def f3(self):
        print("This is Class C functionality")

class D(A,B,C):
    def f4(self):
        print("this is Class D functionality")
obj1 = D()
obj1.f2()

->
class A:
    def __init__(self):
        print("this is class A Constructor")
    def f1(self):
        print("This is Class A Functionality")

class B(A):
    def __init__(self):
        super().__init__()
        print("this is class B Constructor")
    def f2(self):
        print("This is Class B Functionality")

class C(B):
    def __init__(self):
        super().__init__()
        print("this is class C Constructor")
    def f3(self):
        print("This is Class C functionality")

class D(C):
    def __init__(self):
        super().__init__()
        print("This is class D constructor")
    def f4(self):
        print("this is Class D functionality")
obj1 = D()
obj1.f2()

->
class A:
    def __init__(self):
        print("this is class A Constructor")
    def f1(self):
        print("This is Class A Functionality")

class B():
    def f2(self):
        print("This is Class B Functionality")

class C():
    def f3(self):
        print("This is Class C functionality")

class D(A,B,C):
    def __init__(self):
        super().__init__()
        print("This is class D constructor")
    def f4(self):
        print("this is Class D functionality")
obj1 = D()
obj1.f2()

-> polymorphism:
    -> Duck Typing:
    -> operator Overriding:
    -> method overriding:
    -> method overloading:

-> Method over riding :
    class A:
    def __init__(self):
        print("this is class A Constructor")
    def f1(self):
        print("This is Class A Functionality")

class B(A):
    def f1(self):
        print("This is Class B Functionality")


obj1 = B()
obj1.f1()

-> Method Overloading:
class f1:
    def sum(self, m1=None, m2=None,m3=None,m4=None):
        if m1!=None and m2!=None and m3!=None and m4!=None:
            sum = m1 + m2 + m3 + m4
            return sum
        elif m1!=None and m2!=None and m3!=None:
            sum = m1 + m2 + m3
            return sum
        elif m1!=None and m2!=None:
            sum = m1 + m2
            return sum
        elif m1!=None:
            sum = m1
            return sum
        else:
            print("none Value")

obj1 = f1()
print(obj1.sum())
->
class f1:
    def sum(self, m1=None, m2=None,m3=None,m4=None):
        if m1!=None and m2!=None and m3!=None and m4!=None:
            sum = m1 + m2 + m3 + m4
            return sum
        elif m1!=None and m2!=None and m3!=None:
            sum = m1 + m2 + m3
            return sum
        elif m1!=None and m2!=None:
            sum = m1 + m2
            return sum
        elif m1!=None:
            sum = m1
            return sum
        else:
            return "none Value"

obj1 = f1()
print(obj1.sum())

-> Duck Typing:
    ->
class laptop:
    def code(self, ide):
        ide.execute()

class text1:
    def execute(self):
        print("Running")
        print("Decode")
        print("Compling")
        print("Execute")
        print("Spelling Check")

class text2:
    def execute(self):
        print("Running")
        print("Compling")
        print("Spelling Check")


ide = text1()
ide2 = text2()

f2 = laptop()
f2.code(ide2)

-> Iterator :
a = [1,2,3,4,6,5]
b = iter(a)
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

-> generator:
def f1():
    yield 10
    yield 20
    yield 30

f2 = f1()
print(f2.__next__())
print(f2.__next__())
print(f2.__next__())

->
a = "Hello World, Today is beautiful day"
b = iter(a)

print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

def f1():
    a = "Hello world today is beautiful day"
    for x in a:
        yield x

f2 = f1()
print(f2.__next__())
print(f2.__next__())
print(f2.__next__())

-> Exception Handling :
    -> Syntax Error:
        print("hello world)
    -> Logical Error :
        a = 10
        b = 0
        print(a/b)
    -> RunTime Error :
        ->
            a = 6
        b = int(input("Enter The number"))
        print(a/b)

-> try, except, finally:

try:
    a = 5
    b = 2
    print(a/b)
except:
    print("Divison by zero is not possible")
finally:
    print("My condition is ok")

->
try:
    a = 5
    b = int(input("Enter Your Number"))
    print(a/b)
except Exception as e:
    print("Divison by zero is not possible", e)
finally:
    print("My condition is ok")

->
try:
    a = 5
    b = int(input("Enter Your Number"))
    print(a/b)
except ZeroDivisionError as e:
    print("Divison by zero is not possible", e)
except ValueError as e1:
    print("Divison by character not possible", e1)
finally:
    print("My condition is ok")

-> Threading:
    ->
    from threading import *
from time import *

class hello(Thread):
    def run(self):
        for x in range(50):
            sleep(1)
            print("hello")

class hi(Thread):
    def run(self):
        for x in range(50):
            sleep(1)
            print("hi")

obj1 = hello()
obj2 = hi()
obj1.start()
sleep(0.2)
obj2.start()

-> File Handling:
    ->  Read the file
        f1 = open('f1.txt', 'r')
        print(f1.read())

    -> Read the file
        f1 = open('f1.txt', 'rt')
        print(f1.read())


     -> Read file in binary mode
        f1 = open('f1.txt', 'rb')
        print(f1.read())


    ->  f1 = open('f1.txt', 'r')
        f2 = f1.readlines()
        print(f2[1])

    ->
        f1 = open('f1.txt', 'r')
        f2 = f1.readline(10)
        print(f2)

    ->
    f1 = open('f1.txt', 'w')
    f1.write("Hello World")

->
    f1 = open('f1.txt', 'a')
    f1.write("Hello World")
    f2= open('f1.txt', 'r')
    print(f2.read())

-> Numpy Library:
    ->
        from numpy import *
        abc = array([1,2,3,4,5,6,7,8,9], float)
        print(abc)

    ->
    from numpy import *
    abc = array([1,2,3,4,5,6,7,8,9], int)
    print(abc.dtype)

-> linspace:
    ->
    from numpy import *
    f1 = linspace(0,15,100)
    print(f1)

    ->
    from numpy import *
    f1 = logspace(0,15,100)
    print(f1)

    ->
    from numpy import *
    f1 = arange(0,15)
    print(f1)

    ->
    from numpy import *
    f1 = zeros(10)
    print(f1)

    ->
    from numpy import *
    f1 = ones(10)
    print(f1)

    ->
    from numpy import *
    f1 = ones(10, int)
    print(f1)

    ->
    from numpy import *
    f1 = array([1,2,3,4,5,6])
    f2 = array([1,2,3,4,5,6])
    print(f1+f2)

    ->
    from numpy import *
    f1 = array([1,2,3,4,5,6])
    f2 = array([1,2,3,4,5,6])
    print(max(f1))

    ->
    from numpy import *
    f1 = array([1,2,3,4,5,6])
    f2 = array([1,2,3,4,5,6])
    print(concatenate((f1,f2)))

    ->
    from numpy import *
    f1 = array([[1,2,3,4,5,6],[3,2,1,2,3,4]])
    f2 = array([[1,2,3,4,5,6],[12,1,2,3,4,5]])

    print(type(matrix(f1)))

->
from numpy import *
f1 = array([[1,2,3,4,5,6],[3,2,1,2,3,4]])
f2 = array([[1,2,3,4,5,6],[12,1,2,3,4,5]])
print(f1.reshape(6,2))

->
    from numpy import *
    f1 = array([[1,2,3,4,5,6],[3,2,1,2,3,4]])
    f2 = array([[1,2,3,4,5,6],[12,1,2,3,4,5]])
    print(f1+f2)

->
    from numpy import *
    f1 = matrix(array([[1,2,3,4,5,6],[3,2,1,2,3,4]]))
    f2 = matrix(array([[1,2,3,4,5,6],[12,1,2,3,4,5]]))
    print(f1*f2.reshape(6,2))

->
    from numpy import *
    f1 = matrix('1,2,3;3,2,3;1,2,3')
    print(type(f1))

->
    from numpy import *
    f1 = matrix(array([[1, 2, 3, 4, 5, 6], [3, 2, 1, 2, 3, 4]]))
    f2 = matrix(array([[1, 2, 3, 4, 5, 6], [12, 1, 2, 3, 4, 5]]))
    print(f1/f2)


-> Matplotlib
1.Basic Chart
    from matplotlib.pyplot import *
    x=[2001,2002,2003,2004]
    y=[1400,1000,2000,1700]
    plot(x,y)
    show()
2.Title and lables
    from matplotlib.pyplot import *
    x = [2001, 2002, 2003, 2004]
    y = [1400, 1000, 2000, 1700]
    title("sales information \n (in years)")
    xlabel("years")
    ylabel("income(cr)")
    plot(x, y)
    show()

3. Legend
    from matplotlib.pyplot import *
    x = [2001, 2002, 2003, 2004]
    y = [1400, 1000, 2000, 1700]

    x2=[2001,2002,2003,2004]
    y2=[3500,1500,2500,2000]

    title("sales information \n (in years)")
    xlabel("years")
    ylabel("income(cr)")
    plot(x, y,label="company 1")
    plot(x2,y2,label="company 2")
    legend()
    show()
3. cosine graph
    from matplotlib.pyplot import *
    from numpy import *
    x=arange(0.0,2.0,0.01)
    y=cos(2*x*pi)
    plot(x,y,label="cosine graph")
    xlabel("Time(t)")
    ylabel("Voltage(Mv)")
    title("cosine wave plot")
    show()

4.Sin Graph
    from numpy import *
    from matplotlib.pyplot import *
    x=[0,30,45,60,90]
    y=sin(x)
    plot(x,y,marker="*")
    show()

5.Bar graph
    from matplotlib.pyplot import *
    from numpy import  *
    X=["sports","phone","friends","money","online","club","tv"]
    Y=[45,53,99,44,66,25,37]
    xlabel("activities")
    ylabel("no_of_students")
    title("school data\n (palanpur)")
    bar(X,Y,label="palanpur",color="black")
    show()

6. Histograph
from matplotlib.pyplot import *
english=[40,45,52,55,58,60,63,65,69,68,71,72,76,77,78,79,80,81,99,110,104,100]
maths=[42,46,81,75,69,43,85,95,65,70,56,61,84,99,93,100,82,75,63,102]
yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
hist([english,maths],bins=[40,60,80,100,110],color=["red","blue"],rwidth=.95,label=["emarks","mmarks"])
legend()
show()

7.Pie chart
from matplotlib.pyplot import *
slices=[8,3,5,4,2]
activities=["sleep","study","socialmedia","playing","eating"]
pie(slices,labels=activities,colors=["red","yellow","green","blue","orange"],startangle=120,explode=[.2,00,00,0,0],autopct="%1.2f%%",shadow=True)
legend()
show()

8.chart using csv file
from matplotlib.pyplot import *
import csv
x=[]
y=[]

with open("C:\\Users\\abc\\Desktop\\har.txt","r") as csvfile:
    hari=csv.reader(csvfile)
    for i in hari:
        x.append(i[0])
        y.append(i[1])

plot(x,y,label="csv graph",color="red")
legend()
show()

9.sub plots
from matplotlib.pyplot import *
from numpy import *
subplot(2,2,1)
x =arange(1,5)
plot(x,x*x)
title('square')
subplot(2,2,2)
title('square root')
plot(x,sqrt(x))
subplot(2,2,3)
title('exp')
plot(x,np.exp(x))
subplot(2,2,4)
plot(x,np.log10(x))
title('log')
show()

->>> Pandas library
1.
    from pandas import *
    cars=["har","hari","kinjal","papa","mamma"]
    a=Series(cars)
    print(Series(cars))
    print(a.values)
    print(a.dtype)
    print(a.index)

2.
    from pandas import *
    nums=[1,2,3,4,5,6,7,8,9,10]
    a=Series(nums)
    print(a)
    print(a.mean())
    print(a.sum())
    print(a.product())

3.
    from pandas import *
    fruits=["cherry","mango","cheeku","banana","grapes"]
    week_days=["mon","tues","wed","fri","sat"]
    print(Series(fruits,week_days))
    print(Series(data=week_days,index=fruits))

"""
