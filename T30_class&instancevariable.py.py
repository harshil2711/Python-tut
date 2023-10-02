class Employee():
    no_of_leaves = 9  # Class variable


rohan = Employee()
mohan = Employee()


rohan.name = 'Rohan'  # Instance variable
rohan.age = 30 # Instance variable
rohan.job = 'Manager' # Instance variable

mohan.name = 'Mohan' # Instance variable
mohan.age = 40 # Instance variable
mohan.job = 'HOD' # Instance variable


print(rohan.name)
print(rohan.age)
print(rohan.job)
print(rohan.no_of_leaves)

print()

print(mohan.name)
print(mohan.age)
print(mohan.job)
print(mohan.no_of_leaves)

print()

print(Employee.no_of_leaves)

Employee.no_of_leaves = 15  # Changing the class variable . You can change the class variable by using class it self.
rohan.no_of_leaves = 20

print(Employee.no_of_leaves)

print(mohan.__dict__) # It will return the dictionary of the object.
print(rohan.__dict__)



# Output
# Rohan
# 30
# Manager
# 9
#
# Mohan
# 40
# HOD
# 9
#
# 9
# 15
# {'name': 'Mohan', 'age': 40, 'job': 'HOD'}
# {'name': 'Rohan', 'age': 30, 'job': 'Manager', 'no_of_leaves': 20}