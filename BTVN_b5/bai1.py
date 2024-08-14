students = {
    "SV001": 3.2,
    "SV002": 2.8,
    "SV003": 3.5,
    "SV004": 4.0,
    "SV005": 1.9
}

# Đếm số sinh viên có điểm tổng kết trong đoạn [3.0, 3.5]
count_in_range = sum(1 for score in students.values() if 3.0 <= score <= 3.5)
print(f"Số sinh viên có điểm tổng kết trong đoạn [3.0, 3.5]: {count_in_range}")

students["SV006"] = 3.8
print("Đã thêm sinh viên SV006 với điểm tổng kết 3.8")

students = {student_id: score for student_id, score in students.items() if score >= 2.0}

print("Từ điển sinh viên sau khi xử lý:")
for student_id, score in students.items():
    print(f"Mã sinh viên: {student_id}, Điểm tổng kết: {score}")
