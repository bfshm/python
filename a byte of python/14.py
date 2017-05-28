import time

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end = '')
        time.sleep(2)
except KeyboardInterrupt:
    print('you cancelled the reading from the file!')
finally:
    f.close()
    print('closed the file.')

import sys
sys.exit(0)
###############################################

class inputoverflow(Exception):
    def __init__(self, len, max):
        Exception.__init__(self)
        self.len = len
        self.max = max

class inputlimit(Exception):
    def __init__(self, len, min):
        Exception.__init__(self)
        self.len = len
        self.min = min

maxlen = 6
minlen = 3
    
try:
    text = input('enter something:')
    txtlen = len(text)
    if txtlen > maxlen:
        raise inputoverflow(txtlen, maxlen)
    if txtlen < minlen:
        raise inputlimit(txtlen, minlen)
except EOFError:
    print('you do an EOF on me.')
except inputoverflow as ex:
    print('the input was {0} long, atmost {1}!'.format(ex.len, ex.max))
except inputlimit as ex:
    print('the input was {0} long, atleast {1}!'.format(ex.len, ex.min))
else:
    print('no exception')
finally:
    pass

import sys
sys.exit(0)
###############################################

try:
    text = input('enter something:')
except EOFError:
    print('why did you do an EOF on me?')
except KeyboardInterrupt:
    print('you cancel the operation.')
else:
    print('you enderd {0}', text)
finally:
    pass

import sys
sys.exit(0)
###############################################