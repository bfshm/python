import os, platform, logging

if platform.platform().startswith('Windows'):
    #logfile = os.path.join(os.getenv('HOMEDRIVE'), 'test.log')
    logfile = 'test.log'
else:
    logfile = os.path.join(os.getenv('HOME'), 'test.log')

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)7s : %(message)s',
    filename = logfile,
    filemode = 'w',
)

logging.debug('start of the program')
logging.info('doing something')
logging.warning('living now')

import sys
sys.exit(0)
###############################################

import sys, warnings

if sys.version_info[0] < 4:
    warnings.warn("Need Python 3.0 for this program to run", RuntimeWarning)
else:
    print('Proceed as normal')

import sys
sys.exit(0)
###############################################