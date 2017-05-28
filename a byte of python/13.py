import pickle

datafilepath = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(datafilepath, 'wb')
pickle.dump(shoplist, f)
f.close()

f = open(datafilepath, 'rb')
storedlist = pickle.load(f)
print(storedlist)

import sys
sys.exit(0)
###############################################

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt', 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()

import sys
sys.exit(0)
###############################################