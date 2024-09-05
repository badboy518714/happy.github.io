import time

print('hello ---3 world')
print('hello ---4 world')
print('hello world')
print('hello world')

#open('https://raw.githubusercontent.com/badboy518714/happy.github.io/main/output.txt', 'w+').write(f'helloworld{int(time.time()*1000)}')
with open('data/output.txt', 'r') as f:
   a = f.read()
   print(a)
data = 'hello --- world'
with open('data/output.txt', 'w') as f:
   f.write(data)
print('hello ---1 world')
print('hello ---2 world')
