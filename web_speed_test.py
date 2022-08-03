# -*- coding: utf-8 -*-
import requests
import time
urls = ['https://aaaa',
        'https://bbbb',
        'https://cccc',
        'https://dddd']

print(f'Testing started...\r\n')
# test url speed every 10 secs for 5 times in total
with open('speedtest.txt', 'w') as f:
    for n in range(4): 
        print(f'Round {n+1}： \r\n')
        f.write(f'Round {n+1}： \r\n')
        for i in urls: 
            r = requests.get(i) # get response code
            delta_time = r.elapsed.total_seconds() # get response delta time
            time.sleep(10)
            output = f'{i}:    {delta_time}s\r\n'
            print(output)
            f.write(output)
        print(f'Round {n+1} done...\r\n')
        f.write(f'Round {n+1} done...\r\n')


print(f'All tests finished...\n')
