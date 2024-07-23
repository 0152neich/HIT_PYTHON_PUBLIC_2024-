n = int(input())
a = [0, 1]

for i in range(2, n):
    m = a[-1] + a[-2]
    a += [m]

for num in a:
    print(num, end=' ')