
class Shapes:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2


    def area(self):
        print('Shape has no area')

class Triangle(Shapes):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print('Area of Triangle : ',area)

class Rectangle(Shapes):
    def area(self):
        area = self.dim1 * self.dim2
        print('Area of Rectangle : ',area)

s1 = Shapes(10,20)
s1.area()

t = Triangle(20,30)
t.area()

r = Rectangle(20,30)
r.area()




