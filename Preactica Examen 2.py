def tax_deduction(salary, dependents):
    if salary < 18000:
        reduction = 10000
    elif salary < 25000 and dependents >=2:
        reduction = 20000
    elif dependents <2:
        reduction = 10000
    else:
        reduction = 0.75 * salary
    return reduction

salary = 14000
dependents = 3

print "Reduction is $", tax_deduction(salary, dependents)

print "Reduction is $", tax_deduction(60000, 5)

print "Reduction is $", tax_deduction(21000, 3)
