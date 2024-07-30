N = int(input("Nhập số lượng số Nasus có: "))
num = list(map(int, input("Nhập các số: ").split()))

lst = []

for i in num:
    if i % 2 != 0:
        lst.append(i)

lst.sort()  
print(len(lst))
print(" ".join(map(str, lst)))
