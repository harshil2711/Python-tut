class Cricket:
    def __init__(self , name):
        self.name = name     # Public variable


c1 = Cricket('Kohli')

print(c1.name)

# Output
# Kohli

# __________________________________________________________

class Employee:
    def __init__(self,id):
        self._id = id     # Protected variable


e = Employee(758)
print(e._id)

# Output
# 758


# ___________________________________________________________________

class Pm:
    def __init__(self , income):
        self.__income = income  # Private variable

p = Pm(1000)
print(p._Pm__income)

# # Output
# 1000


# _____________________________________________________________________

"""
    Public = It can be used by any class.
    Protected = It can only used by base class and derived class.
    Private = It can only used in this particular class.
"""

class Cricket:
    __income = 50000000     # Private variable , To make private variable just add "__" before variable name.
    _stadium = 200          # Protected variable , To make protectede variable just add "_" before variable name.
    bat = 50                # Public variable

    def __init__(self,name , run , stike_rate):
        self.name = name
        self.run = run
        self.sr = stike_rate

    def playerInfo(self):
        print(f'Name : {self.name}')
        print(f'Run : {self.run}')
        print(f'Srike_rate : {self.sr}')


virat = Cricket('Virat Kohli', 6000 , 200)

virat.playerInfo()

print(virat.bat)

print(virat._stadium)

print(virat._Cricket__income)  # This is the way to access the private variable.


# Output
# Name : Virat Kohli
# Run : 6000
# Srike_rate : 200
# 50
# 200
# 50000000
