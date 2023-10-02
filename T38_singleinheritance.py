"""
    In this single inheritance base class derives the only one parent class.
    In this child class can use all the methods and attribute of parent class.
"""


class Employee:
    company = 'Google'

    def showDetails(self):
        print('this is employee class')

    def greet(self):
        print(f'hello good morning , {self.company}')


class Student(Employee):
    company = 'Youtube'

    def showDetails(self):
        print('this is youtube class')


e = Employee()

e.showDetails()

s = Student()

s.showDetails()

print(e.company)

print(s.company)


s.greet()

# output
# this is employee class
# this is youtube class
# Google
# Youtube
# hello good morning , Youtube
