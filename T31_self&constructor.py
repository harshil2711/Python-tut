class Employee:
    no_of_leaves = 10

    def detail(self):
        print(f"My name is {self.name}. My age is {self.age}. My job is {self.job}")


rohan = Employee()
mohan = Employee()


rohan.name = 'Rohan'  # Instance variable
rohan.age = 30 # Instance variable
rohan.job = 'Manager' # Instance variable

mohan.name = 'Mohan' # Instance variable
mohan.age = 40 # Instance variable
mohan.job = 'HOD' # Instance variable


mohan.detail()
print()
rohan.detail()


# Output
# My name is Mohan. My age is 40. My job is HOD
# My name is Rohan. My age is 30. My job is Manager

# _________________________________________Constructor_____________________________________
# 1. Parameterized constructor

class Student():

    def __init__(self , name , roll , age):
        self.name = name
        self.roll_no = roll
        self.age = age


    def student_detals(self):
        print(f"Students name is {self.name}. Roll no is {self.roll_no}. Age is {self.age}")


tom = Student('tom',50 ,14)
# lathem = Student()

tom.student_detals()

print(tom.name)
print(tom.roll_no)
print(tom.age)


# Output:
# Students name is tom. Roll no is 50. Age is 14
# tom
# 50
# 14

# _____________________________________________________________________

# 2. Default constructor


class Army:

    def __init__(self):
        print("Welcome to the academy")


harry = Army()
mohan = Army()

# Output
# Welcome to the academy
# Welcome to the academy
