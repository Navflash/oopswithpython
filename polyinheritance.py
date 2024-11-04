from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):

    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length ** 2
    

shapes = [Circle(4),Square(4)]

for shape in shapes:
    print(f"{shape.area()} cm^2")