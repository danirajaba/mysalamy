import itertools

from itertools import product
from string import ascii_lowercase, digits
import timeit
import requests
import time
import re

import sys

start = timeit.default_timer()

for item in itertools.product(ascii_lowercase + digits, repeat=9):
    print('a'+''.join(item))
    
stop = timeit.default_timer()
print(f'Time: ', stop - start)  
