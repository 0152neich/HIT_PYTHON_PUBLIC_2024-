def tong_chu_so(n):
    sum_digits = 0
    so = n
    while so != 0:
        sum_digits += so % 10
        so //= 10
    return sum_digits

# Nhập vào giá trị n
n = int(input())

if n < 10:
    print(n, 1)
else:
    a1 = tong_chu_so(n)
    if a1 < 10:
        print(a1, 2)
    else:
        a2 = tong_chu_so(a1)
        if a2 < 10:
            print(a2, 3)
        else:
            a3 = tong_chu_so(a2)
            print(a3, 4)
