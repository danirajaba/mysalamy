from itertools import product
from string import ascii_lowercase, digits
import timeit
import requests
import time


start = timeit.default_timer()
date_ = int(time.time())


for item in product(ascii_lowercase + digits, repeat = 9):
    code = 'a' + ''.join(item)

    url = f""
    status = requests.get(url).status_code

    print(f"{code}: {status}")

    if status == 200:                
        with open(f'output_{date_}.txt', 'a') as file:
            file.write( url + '\n')

stop = timeit.default_timer()
print('Time: ', stop - start)  
