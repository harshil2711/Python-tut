"""
    Multipleinheritance occurs when the child class inherits from more than one parent class.
    Here class Programmer inherits Employee and Student class .
    Here Employee class attributes and method gets first priority because it has been written first.
"""


class Employee:
    name = 'Google'

    def greet(self):
        print('hello world')


class Student:
    name = 'Youtube'
    standards = 10

    def upgradeStandard(self):
        self.standards = self.standards + 1

    def greet(self):
        print('hello people')


class Programmer(Employee, Student):
    company = 'Google'


e = Employee()

p = Programmer()

print(p.standards)

p.upgradeStandard()

print(p.standards)

p.greet()

e.greet()

# Output
# 10
# 11
# hello world
# hello world