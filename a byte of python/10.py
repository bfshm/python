str = '0123456789'

print("str.startswith('012'):", str.startswith('012'))
print("'345' in str:", '345' in str)
print("str.find('678') != -1:", str.find('678') != -1)

delimiter = '_*_'
mylist = ['brazil', 'russia', 'india', 'china']
print(delimiter.join(mylist))

import sys
sys.exit(0)
###############################################

src = '0123456789'
dst = src
src = src[1:]
print(src)
print(dst)

import sys
sys.exit(0)
###############################################

bri = set(['brazil', 'russia', 'india'])
print("bri:", bri)
print("'india' in bri:", 'india' in bri)
print("'usa' in bri:", 'usa' in bri)

bric = bri.copy()
bric.add('china')
print("bric:", bric)
print("bric.issuperset(bri):", bric.issuperset(bri))
print("bri.issubset(bric):", bri.issubset(bric))

brid = bri.copy()
brid.remove('russia')
print("brid:", brid)
print("bric & brid:", bric & brid)
print("bric or brid:", bric or brid)

import sys
sys.exit(0)
###############################################

#slice
print('0123456789'[2:3])
print('0123456789'[::-1])

import sys
sys.exit(0)
###############################################

zoo=('python', 'elephant', 'penguin')
newzoo = ('monkey', 'camel', zoo)

print(newzoo, print(newzoo[2]))
print(len(zoo))
print(zoo)

print(len(newzoo))
print(newzoo)

#slice
print(zoo[1:-1])

import sys
sys.exit(0)
###############################################

def printlist(list):
    for item in list:
        print(item, end=' ')
    print('\r')
    #slice
    print(list[2:-1])

shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'item to purchase.')

print('These items are:')
printlist(shoplist)

shoplist.append('rice')
printlist(shoplist)

shoplist.sort()
printlist(shoplist)

del shoplist[0]
printlist(shoplist)

import sys
sys.exit(0)
###############################################

ab = {
    '1' : '1@1.com',
    '2' : '2@2.com',
    '3' : '3@3.com',
    '4' : '4@4.com',
    '5' : '5@5.com',
    }
print(ab['1'])
del ab['2']
print('{0} contacts:'.format(len(ab)), ab)

import sys
sys.exit(0)
###############################################

