# câu a
n = int(input())
s = 0
for i in range(1, 2*n + 2):
    if i % 2 != 0:
        s += i
    else:
        s -= i
print(s)

# câu b
n = int(input())
sum = 0
for i in range(1,n + 1):
    sum += 1/i
print(sum)

# câu c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print('Phương trình đã cho có vô số nghiệm')
        else:
            print('Phương trình đã cho vô nghiệm')
    else:
        if c == 0:
            print('Phương trình đã cho có nghiệm là 0')
        else:
            print('Phương trình đã cho có nghiệm là', -c/b)
else:
    delta = b*b - 4*a*c
    if delta > 0:
        print('Phương trình đã cho có 2 nghiệm phân biệt là:', end=' ')
        print((-b - delta**0.5) / (2*a), 'và', (-b + delta**0.5) / (2*a))
    elif delta == 0:
        print('Phương trình đã cho có nghiệm kép là', end=' ')
        print(-b / (2*a))
    else:
        print('Phương trình đã cho vô nghiệm')