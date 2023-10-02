"""
    Super keyword is used when you want to run super class and subclass constructor both.
    Here programmer class inherits the Employee class.
    But Programmer class also has the init constructor. So it overwirtes the super class constructor.


"""

class Employee:
    company = 'Google'

    def __init__(self , name , id):
        self.name = name
        self.id = id
        self.rank = 15

    def printInfo(self):
        print(f"My name is {self.name} and my id is {self.id}")


class Programmer(Employee):
    company = "Youtube"
    salary = 55

    def __init__(self , lang):
        super().__init__("harry" , 20)
        self.lang = lang

    def progInfo(self):
        print(f"I know {self.lang}")

p = Programmer("python")


p.printInfo()

print(p.company)

print(p.rank)

# Output
# My name is harry and my id is 20
# Youtube
# 15


# ________________________________________________________________

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")


o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())

