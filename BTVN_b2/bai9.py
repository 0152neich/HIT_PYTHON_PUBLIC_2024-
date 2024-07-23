#9a
a = int(input("Nhập một số nguyên: "))

if a < 0:
    a = -a

if a == 0:
    bit_count = 1
else:
    bit_count = 0
    while a > 0:
        bit_count += 1
        a = a // 2

print("Số lượng bit cần thiết:", bit_count)

#9b
x = 'awesome'
print('Python is ' + x) 
print('Python is {}'.format(x))
print(f'Python is {x}')

#9c
import sys
print(sys.version)

 