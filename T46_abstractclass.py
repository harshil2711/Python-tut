from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self):
        self.height = 10
        self.width = 15

    def area(self):
        return self.height * self.width


r1 = Rectangle()
print(r1.area())

"""
Now here if you not define any method name that has same in abstarctmethod it will give you an error.
So the meaning of the abstract method is that to tell every class should define the same method that in abstarct class.
After define same method in subclass it will not give an error.

YOU CANT CREATE THE OBJECT OF THE ABSTRACT METHOD.
"""
# Output
# 150