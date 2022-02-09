import abc          #abstract base class
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):         #abstract method declaration
        pass
class Rectangle(Shape):
    def __init__(self, x,y):
        self.l = x
        self.b = y
    def area(self):
        return self.l+self.b
r = Rectangle(10,20)
print('area: ', r.area())




