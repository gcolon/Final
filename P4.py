def pay_rise(current_salary):
    new_salary = 0
    if current_salary < 20000:
        new_salary = current_salary * 1.10
    else:
        new_salary = current_salary * 1.07
    return new_salary

pete_salary = 19000
bob_salary = 40000

print "New Pete Salary - ", pay_rise(pete_salary)
print "New Bob Salary - ", pay_rise(bob_salary)


