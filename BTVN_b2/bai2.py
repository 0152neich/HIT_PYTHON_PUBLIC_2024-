# Nhập vào hai số nguyên
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# 2a: Tính tổng của a và b
print("Tổng a + b:", a + b)

# 2b: Tính hiệu của a và b
print("Hiệu a - b:", a - b)

# 2c: Tính tích của a và b
print("Tích a * b:", a * b)

# 2d: Tính thương của a chia cho b (chia nguyên)
print("Thương a // b:", a // b)

# 2e: Tính lũy thừa của a mũ b
print("Lũy thừa a ** b:", a ** b)

# 2f: Tính số dư khi a chia cho b
print("Số dư a % b:", a % b)

# 2g: So sánh a và b
if a - b > 0:
    print('a lớn hơn b')
elif a - b < 0:
    print('a nhỏ hơn b')
else:
    print('a bằng b')

# 2h: Phép toán AND giữa a và b
print("a & b:", a & b)

# 2i: Phép toán OR giữa a và b
print("a | b:", a | b)

# 2j: Phép toán XOR giữa a và b
print("a ^ b:", a ^ b)

# 2k: So sánh không bằng giữa a và b
print("not(a == b):", not(a == b))

# 2l: Phép dịch phải bit của a
print("a >> 1:", a >> 1)

# 2m: Phép dịch trái bit của a
print("a << 1:", a << 1)
