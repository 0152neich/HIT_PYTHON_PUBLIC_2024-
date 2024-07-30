s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

# In ra đảo ngược của chuỗi s1
s1_reversed = s1[::-1]
print(f"Chuỗi s1 đảo ngược:{s1_reversed}")

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Đảo ngược chuỗi từ vị trí a đến b trong s2 và in ra
s2_reversed_v2 = s2[:a] + s2[a:b+1][::-1] + s2[b+1:]
print("Chuỗi s2 sau khi đảo ngược từ vị trí", a, "đến", b, ":", s2_reversed_v2)

# In ra chuỗi s3 là chuỗi s1 sau khi xóa các ký tự vị trí chẵn
s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 != 0])
print("Chuỗi s3 sau khi xóa các ký tự vị trí chẵn:", s3)

# Trả về chuỗi s4 là đan xen các ký tự của s1 và s2
s4 = ''.join(a + b for a, b in zip(s1, s2))
s4 += s1[len(s2):] if len(s1) > len(s2) else s2[len(s1):]
print("Chuỗi s4 đan xen các ký tự của s1 và s2:", s4)

# Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
new_s1 = s2[0] + s1[1:]
new_s2 = s1[0] + s2[1:]
print("Chuỗi s1 và s2 sau khi đổi chỗ ký tự đầu tiên:", new_s1, "và", new_s2)
