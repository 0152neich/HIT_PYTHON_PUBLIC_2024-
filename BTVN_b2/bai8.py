N = int(input("Nhập vào số hàng của tam giác Pascal: "))

for i in range(N):
    value = 1
    for j in range(i + 1):
        print(value, end=' ')
        value = value * (i - j) // (j + 1)
    print()

# Tham khảo cách làm dùng thư viện math 
# from math import *
# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print(comb(i,j),end=' ')
#     print('\n')
