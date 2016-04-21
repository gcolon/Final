L = [0,-2,100,200,4]

def max_number(L):
    max = L[0]
    for n in L:
       if n > max:
           max = n
    return max

print "Max = ", max_number(L)

