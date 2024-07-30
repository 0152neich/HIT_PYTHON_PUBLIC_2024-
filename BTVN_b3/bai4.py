name = input("Nhập họ và tên: ")

standard_name = [ch.capitalize() for ch in name.split()]
format_name = ' '.join(standard_name)

print(f"Họ và tên đã được chuẩn hóa:{format_name}")
