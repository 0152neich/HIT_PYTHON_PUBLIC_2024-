A = {"SV001", "SV002", "SV003", "SV004"}
B = {"SV003", "SV005", "SV006", "SV007"}

print("Danh sách sinh viên tại bàn 1:", A)
print("Danh sách sinh viên tại bàn 2:", B)

# Kiểm tra có sinh viên nào đăng ký học tại cả hai bàn
sinh_vien_ca_hai_ban = A.intersection(B)
if sinh_vien_ca_hai_ban:
    print("Có sinh viên đăng ký học tại cả hai bàn:", sinh_vien_ca_hai_ban)
else:
    print("Không có sinh viên nào đăng ký học tại cả hai bàn.")

# Danh sách tổng hợp các sinh viên đã đăng ký của cả hai bàn
danh_sach_tong_hop = A.union(B)
print("Danh sách tổng hợp các sinh viên đã đăng ký của cả hai bàn:", danh_sach_tong_hop)

# Danh sách các sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn 2
sinh_vien_chi_ban_1 = A.difference(B)
print("Danh sách sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn 2:", sinh_vien_chi_ban_1)
