# Define a circle by Point(x, y) and Radius

# Draw the circle
# PI = 3.1415

# point1 = 5
# point2 = 5

class Point:
    def __init__ (self, point1, point2):
        self._point1 = point1
        self._point2 = point2
        point1 = 5
        point2 = 5
    def point1(self, p1 = None):
        if p1:
            self._point1 = p1
            return self._point1

    def point2(self, p2 = None):
        if p2:
            self._point2 = p2
            return self._point2

class Circle(Point):




    def radius(self, radius):
        self._radius = radius 
        radius = 3


    def drawCircle(self, point1, point2):
        col = (self.point1)**2
        Row = (self.point2)**2
        for i in range(0, col):
            for j in range(0, Row):
                if(i == 0 or i == Row - 1 or j == 0 or j == col - 1):
                    print("*", end= " ")
                else:
                    print(" ")
        super().__init__(point1, point2)
    # def area(self, a = None):
    #     if a:
    #         self._area = a 
        
    #         return self._radius**2*3.141

    


    # def area(self)
    #     print(Circle.PI * self._radius * self._radius)
        
#     def __str__(self):
#         return f'Circle is on point{self.point1()}, {self.point2()}'

# circle = Circle(point1 = "3", point2 = "3")

# print(circle)
