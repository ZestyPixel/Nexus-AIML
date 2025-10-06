#Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p1 = Point(2, 3)
p2 = Point(5, 7)
p3 = p1 + p2
p4 = p2 - p1
print(p3)  
print(p4)
