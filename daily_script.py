import time

print('hello world')
print('hello world')
print('hello world')
print('hello world')

open('./output.txt', 'w+').write(f'helloworld{int(time.time()*1000)}')
