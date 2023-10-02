# Class methods are used to change the class variable.


class Employee:
    no_of_leaves = 10

    def showDetails(self):
        print(f"The no of leaves are {self.no_of_leaves}")

    @classmethod
    def chnageLeaves(cls , newleaves):
        cls.no_of_leaves = newleaves


emp1 = Employee()

emp1.showDetails()

Employee.chnageLeaves(500)

emp1.showDetails()