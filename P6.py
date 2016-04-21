class Person(object):
    def __init__(self, id, first_name, last_name, age, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone

    def __str__(self):
        return "[%s, %s, %s, %s, %s]" % (self.id, self.first_name, self.last_name, self.age, self.phone)

###### Test
joe = Person("1", "Joe", "Smith", 23, "787-890-2020")
print "Joe age:", joe.age
print "Joe phone:", joe.phone
print "Joe =", joe





