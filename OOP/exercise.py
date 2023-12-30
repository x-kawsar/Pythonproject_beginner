
# Triangle
class Triangle():

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate(self):
        area = 0.5 * self.base * self.height
        print('Triangle is : ',area)


t1 = Triangle(20,10)
t1.calculate()

t2 = Triangle(20,30)
t2.calculate()




