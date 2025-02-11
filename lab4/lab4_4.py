class parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

base = 5
height = 6

parallelogramm = parallelogram(base, height)

area = parallelogramm.area()

print(f"Length of base: {base}")
print(f"Height of parallelogram: {height}")
print(f"Expected Output: {area:.1f}")