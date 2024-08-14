input_string = input("Nhập chuỗi: ")

char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Từ điển ký tự và số lần xuất hiện:")
print(char_count)
