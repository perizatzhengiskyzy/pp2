import math

class converter:
    def __init__(self, degree):
        self.degree = degree

    def degree_to_radian(self):
        return self.degree * (math.pi / 180)

degree = 15 
converter = converter(degree)
radian = converter.degree_to_radian()

print(f"Input degree: {degree}")
print(f"Output radian: {radian:.6f}")