class Employee:
    company = 'Google'

    def __init__(self , name):
        self.name = name


    def printInfo(self):
        print(f'My name is {self.name}.')


    @staticmethod     #It is used to use the method without self keyword.
    def greet(name):
        print(f'Hello good morning {name}.')


a = Employee('Brahma')

a.printInfo()

Employee.greet('Harshil')    # You can access static method with class name also.

a.greet('Mahesh')    # You can access static method with object also.