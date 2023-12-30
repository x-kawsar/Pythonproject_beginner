
class Studen():
    roll = ''
    gpa = ''

    # Construcktor
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa  = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

kawsar = Studen(10,3.6)

kawsar.display()

hasan = Studen(20,3)

hasan.display()


naim = Studen(25,4)

naim.display()











