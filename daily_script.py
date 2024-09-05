import time

print('hello --- world')
print('hello --- world')
print('hello world')
print('hello world')

#open('https://raw.githubusercontent.com/badboy518714/happy.github.io/main/output.txt', 'w+').write(f'helloworld{int(time.time()*1000)}')
with open('data/output.txt', 'r') as f:
   a = f.read()
   print(a)
with open('requirements.txt', 'r') as f:
   a = f.read()
   print(a)
print('hello ---1 world')
print('hello ---2 world')
