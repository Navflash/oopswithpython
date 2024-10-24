
class Shapes:
    def __init__(self,colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"shape is {self.colour} and {'filled' if self.is_filled is True else 'not_filled'}.")

class Circle(Shapes):
    def __init__(self, colour, is_filled,radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
        print(f"circle area is {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shapes):
    def __init__(self, colour, is_filled,length):
        super().__init__(colour, is_filled)
        self.length = length

circle = Circle(colour="red",is_filled=True,radius=5)
square = Square(colour="blue",is_filled=False,length=2)

#print(circle.colour,circle.is_filled,circle.radius)
#print(square.colour,square.is_filled,square.length)
#square.describe()
circle.describe()