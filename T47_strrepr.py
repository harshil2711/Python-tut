"""
    __methods__ are dunder methods.
    str has the highest priority than repr.
    If you have both and you want to call repr then do print(repr(e1)).

"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printInfo(self):
        print("Infor")

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return "This is repr method"

    def __str__(self):
        return "This is str method"


e1 = Employee('rohan', 50)

e2 = Employee('Mohan', 60)

e3 = Employee('Naresh', 40)

print(e1 + e2)

print(e1 / e2)

print(e1)

print(str(e1))

print(repr(e1))

# Output
# 110
# 0.8333333333333334
# This is str method
# This is str method
# This is repr method