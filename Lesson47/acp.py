from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def display(self):
        pass

# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def display(self):
        print(f"Rectangle Area: {self.area()}")

# Square class
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def display(self):
        print(f"Square Area: {self.area()}")

# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def display(self):
        print(f"Triangle Area: {self.area()}")

# Circle class
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def display(self):
        print(f"Circle Area: {self.area():.2f}")

# Demo / Testing
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Square(7),
        Triangle(6, 4),
        Circle(3)
    ]

    for shape in shapes:
        shape.display()
