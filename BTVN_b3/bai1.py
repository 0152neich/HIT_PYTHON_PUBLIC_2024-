N = int(input("Nhập số lượng phần tử N: "))
lst = []
for _ in range(N):
    num = int(input(f"Nhập phần tử {_ + 1}: "))
    lst.append(num)

X = int(input("Nhập số X: "))
cnt = lst.count(X)
print(f"Số {X} xuất hiện {cnt} lần trong list.")

# Thay thế phần tử từ vị trí 2 -> 7 bằng [8, 5, 4, 0, 1, 3]
lst[1:7] = [8, 5, 4, 0, 1, 3]

# Tìm số lớn nhất và nhỏ nhất trong list sau khi thay thế
max_val = max(lst)
min_val = min(lst)
print(f"Số lớn nhất trong list là {max_val}")
print(f"Số nhỏ nhất trong list là {min_val}")

# Nhập số Y và chèn vào đầu list
Y = int(input("Nhập số Y: "))
lst.insert(0, Y)

# Kiểm tra sắp xếp
if lst == sorted(lst):
    print("TĂNG")
elif lst == sorted(lst, reverse=True):
    print("GIẢM")
else:
    print("NO")

new_lst = []
for i in range(1, N + 1):
    sum_i = sum(lst[:i])
    new_lst.append(sum_i)
print("List mới với tổng i phần tử đầu tiên của list cũ:", new_lst)

# Tạo list mới và sắp xếp theo thứ tự tăng dần và giá trị tuyệt đối
lst2 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
sorted_lst2 = sorted(lst2)
sorted_abs_lst2 = sorted(lst2, key=abs)

print("List mới sắp xếp theo thứ tự tăng dần:", sorted_lst2)
print("List mới sắp xếp theo giá trị tuyệt đối tăng dần:", sorted_abs_lst2)
