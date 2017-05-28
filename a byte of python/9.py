import this
print(this.__doc__)
#print(this.__name__)

import sys
sys.exit(0)


import module
module.say()
print('version:', module.__version__)

if __name__ == '__main__':
    print('run by self')
else:
    print('run by other')

import os
print(os.getcwd)

import sys
print('agrv are:')
for i in sys.argv:
    print(i)

print('sys path is:', sys.path)


__version__ = '0.1'



