# câu a
n = int(input("Nhập vào 1 số nguyên dương: "))
tong = sum(int(i) for i in str(n))
print(tong)

# câu b
m = int(input("Nhập vào 1 số nguyên dương: "))
tong = 0

for i in range(1, m + 1):
    if n % i == 0:
        tong += i

print(f"Tổng các ước số của {m} là: {tong}")

# câu c
a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c and c == a:
        print('Đây là tam giác cân')
    elif a == b == c:
        print('Đây là tam giác đều')
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("Đây là tam giác vuông")
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2:
        print("Đây là tam giác tù")
    else:
        print("Đây là tam giác nhọn")
else:
    print("2 số a b c không tạo thành tam giác")
