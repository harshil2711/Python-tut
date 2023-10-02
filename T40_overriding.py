"""
                                ATTRIBUTE OVERRIDING
    [[[[[[[[[[[[[ IN case when you have no init constructor in sub class]]]]]]]]]]]]]]]]
    In this example class B inherits all the methods and attributes of the class A.
    Now class A and class B has same name.
    But when you access methods and attributes with the class B object then priority will be below.
    -> Instance variable of A
    -> Class variable of B
    -> Class variable of A

"""


class A:
    classvar1 = 'This is class variable 1'

    def __init__(self):
        self.classvar1 = 'This is instance variable 1'

class B(A):
    classvar1 = 'This is. a class variable 2'


a = A()

b = B()

print(b.classvar1)


# _________________________________________________________________________________________________________

"""
                            METHOD OVERRIDING
    [[[[[[[[[[[[[ IN case when you have init constructor in sub class]]]]]]]]]]]]]]]]
    If you have init constructor in subclass then it overrides the super class constructor.
    In this case it will search for below methods.
    -> Instance variable in class 2
    -> Class variable in class 2
    -> Instance variable in class 1
    -> Class variable in class 1

"""


class Employee:
    classvar = "Class variable 1"

    def __init__(self):
        self.classvar = 'Instace variable 1'

class Programmer(Employee):
    classvar = "Class variable 2"

    def __init__(self):
        self.company = 'Google'
        self.classvar = 'Instance variable 2'


e = Employee()
p = Programmer()


print(p.classvar)