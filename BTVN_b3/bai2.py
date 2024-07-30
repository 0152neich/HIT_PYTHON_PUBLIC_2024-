k = int(input("Nhập số lượng phần tử k: "))
a = []
for i in range(k):
    num = int(input(f"Nhập phần tử {i + 1}: "))
    a.append(num)

n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

if n * m > k:
    print("NO")
else:
    matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        matrix.append(row)
    
    print("Ma trận thu được:")
    for row in matrix:
        print(row)
