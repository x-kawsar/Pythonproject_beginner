
class Studen():
    roll = ''
    gpa = ''

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa  = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

kawsar = Studen()

kawsar.set_value(10,5)
kawsar.display()

hasan = Studen()
hasan.set_value(20,3.50)
hasan.display()


naim = Studen()
naim.set_value(15,35)
naim.display()











