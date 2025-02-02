import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

if __name__ == "__main__":
    point1 = Point(1, 2)
    point1.show() 
    
    point2 = Point(4, 6)
    point2.show()  
    
    point1.move(3, 2) 
    point1.show()  
    
    distance = point1.dist(point2) 
    print(f"Distance between points: {distance}") 
