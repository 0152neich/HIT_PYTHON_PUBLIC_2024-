n = int(input("Nhập số lượng phần tử trong mảng a: "))

a = []
for i in range(n):
    x = input(f"Nhập phần tử thứ {i+1}: ")
    a.append(x)

b = tuple(a)
print("Tuple b:", b)

cnt = 0
for item in b:
    if item.isdigit():  # Kiểm tra nếu toàn bộ các ký tự là số
        cnt += 1

print(f"Số phần tử trong tuple b có dạng số: {cnt}")