from string import ascii_lowercase, digits
import requests
import itertools
import concurrent.futures
import time


alphabet = ascii_lowercase + digits
word_length = 9

date_ = int(time.time())

def generate_urls():
    for combination in itertools.product(alphabet, repeat=word_length):
        code = 'a' + ''.join(combination)
        yield f""

def get_status_code(url):
    print(url)
    response = requests.get(url)
    return (url, response.status_code)

with concurrent.futures.ThreadPoolExecutor(max_workers=2000000) as executor:
    results = list(executor.map(get_status_code, generate_urls()))

for url, status_code in results:
    print(f'{url} returned a status code of {status_code}')
    if status_code == 200:                
        with open(f'output_{date_}.txt', 'a') as file:
            file.write( url + '\n')
  
