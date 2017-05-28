print('8-----------------------------------')

import sys
sys.exit(0)

print('7-----------------------------------')

for i in range(0,16,5):
    print(i)
else:
    print('done')

num = 23
flag = False
while not flag:
    guess = int(input('Enter an integer:'))

    if guess == num:
        print('==')
        flag = True
    elif guess < num:
        print('<')
    else:
        print('>')
else:
    print('Done')

print('6-----------------------------------')
num=23
guess=int(input('Enter an integer: '))

if guess == num:
    print('==')
elif guess < num:
    print('<')
else:
    print('>')

print('done')

#print("hello!")

#如果要严格使用ASCII 编码的字节流，可用str.encode("ascii")
#str = "陈显锋"
#str.encode("ascii")
#print(str)

#你可以在三引号中自由的使用单引号和双引号

#单引号转义 \’s

#format
age=25
name='shane'
print('{0} is {1} years old.'.format(name, age))

area = 5*2
print('area is ', area)