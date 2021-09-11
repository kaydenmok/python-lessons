# Define a circle by Point(x, y) and Radius

# Draw the circle
# PI = 3.1415
import math

# point1 = 5
# point2 = 5

class Point:
    def __init__ (self, x, y):
        self._x = x
        self._y = y

    def x(self, p1 = None):
        if p1 != None:
            self._x = p1
        return self._x

    def y(self, p2 = None):
        if p2 != None:
            self._y = p2
        return self._y

    def __str__(self):
        return f'x: {self._x}, y: {self._y}'

class Circle:
    def __init__(self, point: Point, radius: int):
        self._point: Point = point
        self._radius: int = radius

    def radius(self, radius = None):
        if(radius != None):
            self._radius = radius

        return self._radius

    def point(self, point: Point = None):
        if(point != None):
            self._point = point

        return self._point


    def drawCircle(self):
        radius = self.radius()
        col = row = radius * 2 + 1
        for i in range(0, col):
            for j in range(0, row):
                if(i == 0 or i == row - 1 or j == 0 or j == col - 1):
                    if(i == 0 and (j == 0 or j == 1 or j == col - 2 or j == col - 1)):
                        print(end="  ")
                    elif(i == 1 and (j == 0 or j == col - 1)):
                        print(end="  ")

                    elif(i == row - 1 and (j == 0 or j == 1 or j == col - 2 or j == col - 1)):
                        print(end="  ")
                    elif(i == row-2 and (j == 0 or j == col - 1)):
                        print(end="  ")
                    else: 
                        print(end= "* ")
                elif(i == 1 and (j == 1 or j == col -2) or i == row - 2 and (j == col - 2 or j == 1)):
                    print(end="* ")
                else:
                    print(end = "  ")
                    
            print()
    
    def area(self):
        return self._radius**2*math.pi

    


    # def area(self)
    #     print(Circle.PI * self._radius * self._radius)
        
#     def __str__(self):
#         return f'Circle is on point{self.point1()}, {self.point2()}'
point = Point(3, 3)
print(point)
circle = Circle(point, 4)
# print(circle.point().x())
circle.drawCircle()
# print(circle)
print(circle.area())