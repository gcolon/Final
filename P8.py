class ComplexNumber(object):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + " + " + str(self.b) + "i"

    def conjugate(self):
        return ComplexNumber(self.a, -1*self.b)

    def add(self,N):
        return ComplexNumber(self.a + N.a, self.b + N.b)

    def substract(self, N):
        real = self.a - N.a
        imaginary = self.b - N.b
        return ComplexNumber(real, imaginary)

## Test
c1 = ComplexNumber(2, 4)
c2 = ComplexNumber(-9, 20)

print "c1 =", c1
print"c1 conjugate =", c1.conjugate()
print "c2 =", c2
print"c2 conjugate =", c2.conjugate()

print "c1 + c2 =", c1.add(c2)
print "c1 + c1 conjugate =", c1.add(c1.conjugate())

print "c1 - c2 =", c1.substract(c2)
print "c1 - c1 conjugate =", c1.substract(c1.conjugate())
