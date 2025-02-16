class trapezoid:
    def __init__(self, h, a, b):
        self.h = h
        self.a = a
        self.b = b
    
    def area(self):
        return ((self.a + self.b) * self.h) / 2
h = 5
a = 5
b = 6

t = trapezoid(h, a, b)
area = trapezoid.area(t)
print(f"Height: {h}")
print(f"Base 1, first value: {a}")
print(f"Base 2, second value: {b}")
print(f"Expected Output: {area}")