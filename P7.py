import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
         return "C("+ str(self.radius)+")"

    def circumference(self):
        return 2*math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius

#### Test
circle1 = Circle(10)
print "Circle1 radius:", circle1.radius
print "Circle 1:", circle1
print "Circumference:", circle1.circumference()
print "Area:", circle1.area()
