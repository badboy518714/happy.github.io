import time

print('hello world')
print('hello world')
print('hello world')
print('hello world')

#open('https://raw.githubusercontent.com/badboy518714/happy.github.io/main/output.txt', 'w+').write(f'helloworld{int(time.time()*1000)}')
with open('output.txt', 'w+') as f:
   f.write('helloworld')
