import math

class regular_polygon:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length
    def area(self):
        return (self.sides * self.length ** 2 ) / (4 * math.tan(math.pi / self.sides))

sides = 4
length = 25

polygon = regular_polygon(sides, length)
area = polygon.area()

print(f"Input number of sides: {sides}")
print(f"Input the length of a side: {length}")
print(f"The area of the polygon is: {int(area)}")