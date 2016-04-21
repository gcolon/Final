def positive_sum(L):
    sum = 0
    for n in L:
        if n > 0:
            sum = sum + n
        else:
            sum = sum
    return sum

L = [-1, 2, 14, 0, 0, 1]
print "Sum L:", positive_sum(L)

M = [1, 1, 2, 8, 1]
print "Sum M:", positive_sum(M)

N = [-1, -2, -3]
print "Sum N:", positive_sum(N)


