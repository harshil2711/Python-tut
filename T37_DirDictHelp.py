# DIR is helps us to tell how many methods are with this function. Like here is list.

x = [1,2,3]

print(dir(x))

# Output
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# _______________________________________________________________________________________________________________________________________

# Dict is used to print all the attribute of the class in one dictonary.

class Emp:
    leave = 32

    def __init__(self , name , age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(f"My name is {self.name} and my age is {self.age}")


emp1 = Emp("harshil" , 20)

print(emp1.__dict__)

# Output
# {'name': 'harshil', 'age': 20}

# __________________________________________________________________________________________
# Help function is helps us to get documentation including description.

class Emp:
    leave = 32

    def __init__(self , name , age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(f"My name is {self.name} and my age is {self.age}")


emp1 = Emp("harshil" , 20)

help(Emp)


# Output:
# Help on class Emp in module __main__:
#
# class Emp(builtins.object)
#  |  Emp(name, age)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, age)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  printInfo(self)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  leave = 32
