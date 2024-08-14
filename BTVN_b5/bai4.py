CONFIG = {
    'n': 1500,
    'm': 2,
    'CLUSTERS': 3,
    'ITER': 10000,
    'METHOD': 'FCM',
    'MEASURE': 'EUCLIDEAN',
    'YEARS': 51
}

print("Cấu hình ban đầu:")
print(CONFIG)

# Sửa thông số MEASURE thành "MANHATAN" và in kết quả
CONFIG['MEASURE'] = 'MANHATAN'
print("\nSau khi sửa MEASURE thành 'MANHATAN':")
print(CONFIG)

# In giá trị của thông số METHOD
print("\nGiá trị hiện tại của METHOD là:", CONFIG['METHOD'])

# Bổ sung thêm thông số "LOSS FUNCTION" với giá trị "NORM_2" và in kết quả
CONFIG['LOSS FUNCTION'] = 'NORM_2'
print("\nSau khi thêm 'LOSS FUNCTION':")
print(CONFIG)

# Xóa thông số YEARS và in kết quả
del CONFIG['YEARS']
print("\nSau khi xóa 'YEARS':")
print(CONFIG)

# Nhập một xâu S từ bàn phím và kiểm tra xem S có trùng với giá trị của thông số nào không
S = input("\nNhập một xâu S để kiểm tra: ")
if S in CONFIG.values():
    print(f"S ({S}) trùng với giá trị của một thông số trong CONFIG.")
else:
    print(f"S ({S}) không trùng với giá trị của bất kỳ thông số nào trong CONFIG.")

# Tạo một set chứa toàn bộ giá trị của các thông số trong CONFIG và in kết quả
config_values_set = set(CONFIG.values())
print("\nSet chứa các giá trị của các thông số:")
print(config_values_set)

# Tạo một list chứa toàn bộ giá trị của các thông số trong CONFIG và in kết quả
config_values_list = list(CONFIG.values())
print("\nList chứa các giá trị của các thông số:")
print(config_values_list)