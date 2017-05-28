class schooler:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def tell(self):
        print('name:"{0}" age:"{1}"'.format(self.name, self.age), end=' ')

class teacher(schooler):
    def __init__(self, name, age, salary):
        schooler.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{0})'.format(self.name))

    def tell(self):
        schooler.tell(self)
        print('Salary:"{0:d}"'.format(self.salary))

class student(schooler):
    def __init__(self, name, age, marks):
        schooler.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student:{0})'.format(self.name))
    
    def tell(self):
        schooler.tell(self)
        print('Marks:"{0:d}"'.format(self.marks))

t = teacher('Mrs.Shrividya',30,30000)
s = student('Swaroop',15,75)

print()
members = [t, s]
for m in members:
    m.tell()

import sys
sys.exit(0)
###############################################

class crobot:
    population = 0

    def __init__(self, name):
        self.name = name
        crobot.population += 1
    
    def __del__(self):
        crobot.population -= 1
        if crobot.population == 0:
            print('{0} was the last one'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.format(crobot.population))

    def sayhi(self):
        print('Greetings, my master call me {0}'.format(self.name))

    def howmany(crobot):
        print('We have {0:d} robots.'.format(crobot.population))

    #s_howmany = staticmethod(howmany)

droid1 = crobot('R2-D2')
droid1.sayhi()
crobot.howmany(crobot)

droid2 = crobot('c-3P0')
droid2.sayhi()
crobot.howmany(crobot)

del droid1
del droid2

import sys
sys.exit(0)
###############################################

class cperson:
    def __init__(self, name):
        self.name = name
    def sayhi(self):
        print('hi!', self.name)
    #pass # empty block

p = cperson('Shane')
p.sayhi()

import sys
sys.exit(0)
###############################################