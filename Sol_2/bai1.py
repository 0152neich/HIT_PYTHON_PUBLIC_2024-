def sum_of_numbers_in_string(input_string):
    total_sum = 0
    current_number = ''
    
    for i, char in enumerate(input_string):
        if char.isdigit():  # Nếu là ký tự số
            current_number += char
        elif char == '-' and (i == 0 or not input_string[i - 1].isdigit()):
            # Nếu là dấu '-' và ký tự trước nó không phải là số, gắn dấu âm vào số tiếp theo
            current_number = '-'
        else:
            # Nếu gặp ký tự không phải số, chuyển current_number thành số và cộng vào tổng
            if current_number:
                total_sum += int(current_number)
                current_number = ''
    
    # Cộng nốt số cuối cùng nếu có
    if current_number:
        total_sum += int(current_number)
    
    return total_sum

input_string = input("Nhập chuỗi: ")
result = sum_of_numbers_in_string(input_string)
print(f"Tổng các số trong chuỗi là: {result}")
