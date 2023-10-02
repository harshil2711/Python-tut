class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id


    def showDetails(self):
        print(f"Employee name is {self.name} and id is {self.id}")


e = Employee("Rohan" , 800)
e.showDetails()

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

p = Programmer('mohan' , 40)
p.showDetails()
p.showLanguage()


# Output
# Employee name is Rohan and id is 800
# Employee name is mohan and id is 40
# The default language is Python
