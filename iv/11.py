list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
list3 = list1 + list2
list3.sort()
print(list3)
list4 = []
if len(list3) > 0:
    y = list3[0]
    list4.append(y)
    for x in list3:
        if x == y:
            continue
        y = x
        list4.append(y)
print(list4)

import sys
sys.exit()

st = 'abcdef'
print(st[::-1])

import sys
sys.exit()

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

import sys
sys.exit()

list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

import sys
sys.exit()

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3