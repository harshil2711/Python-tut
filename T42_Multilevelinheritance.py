"""
    When child class becomes parent for another child class.
    In this example all attributes and methods of person inherits in the employee class.
    In this example all attributes and methods of Employee inherits in the programmer class.
    At the end all the attributes and methods of Person class and Employee class inherits in the Programmer class.
"""


class Person:
    country = "INDIA"

    def sleeps(self):
        print('I sleep 8 hrs everyday')


class Employee(Person):
    company = 'Google'

    def works(self):
        print('I work 9 hrs daily')

    def sleeps(self):
        print('I sleep 10 hrs everyday')


class Programmer(Employee):
    company = "Microsoft"

    def coding(self):
        print("I do code for 3 hrs daily")


p = Person()
e = Employee()
pr = Programmer()

print(pr.country)

p.sleeps()

e.sleeps()

pr.sleeps()

# ********************************************************
# Output:
# INDIA
# I sleep 8 hrs everyday
# I sleep 10 hrs everyday
# I sleep 10 hrs everyday
# ********************************************************