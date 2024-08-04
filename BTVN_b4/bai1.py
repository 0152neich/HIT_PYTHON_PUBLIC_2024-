n = int(input())
tuple_of_strings = (input() for _ in range(n))

tuple_of_numbers = tuple(int(num_str) for num_str in tuple_of_strings)

average = sum(tuple_of_numbers) / len(tuple_of_numbers)

# In kết quả
print("Tuple mới gồm các số:", tuple_of_numbers)
print("Trung bình cộng:", average)
