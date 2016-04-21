import math
from math import sqrt
def find_hypotenuse(a,b):
    a_squared = a * a
    b_squared = b * b
    leg_sum = a_squared + b_squared
    return sqrt(leg_sum)
a=3
b=4
hypotenuse = find_hypotenuse(a,b)
print hypotenuse

def print_name(name):
    print "Person name: " + name

print_name("Jose Colon Calderon")
print_name ("Glorymar Colon Torres")

