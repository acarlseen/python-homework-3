class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius
        self.diameter = 2 * radius
    
    def circumference(self):
        return 3.14159 * self.diameter
    
    def area(self):
        return (3.14159) * (self.radius**2)
    
