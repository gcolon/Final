x = 10
if x< 100:
    print x

if x < 1:
    print x

name = "Joe"
if name == "Joe":
    print "Name:",name

if name < "Apu" :
    print "Apu goes first"

if x < 100:
    print x
else:
    print 100

if x < 100:
    print x
else:
    print 100

x = 1000
if x < 100:
    print x
else:
    print 100

name = "Jil"
if name == "Bob":
    print "Hi Bob"
else:
    print "Hi " + name

name1= "Apu"
name2= "Ned"
if name1 < name2:
    print name1
else:
    print name2

def absolute (N):
    if N < 0:
        return -1 * N
    else:
        return N

print "|-1| =", absolute(-1)
print "|100| =", absolute(100)
print "|0| =", absolute(0)

x = 9
if x <0 :
    print "Negative"
elif x == 0:
    print "Zero"
else:
    print "Positive"

x = 0
if x < 0:
    print "Negative"
elif x==0:
    print "Zero"
else:
    print "Positive"

def get_tax_amount(salary):
    if salary < 20000:
        return 0
    elif salary >= 20000 and salary <50000:
        return salary * 0.15
    elif salary >= 50000 and salary < 100000:
        return salary * 0.20
    else:
        return salary * 0.33
print "Bob's Tax - ", get_tax_amount(30000)
print "Jil Tax - ", get_tax_amount(45000)
print "Apu Tax - ", get_tax_amount(130000)
print "Tom Tax - ", get_tax_amount(17000)
