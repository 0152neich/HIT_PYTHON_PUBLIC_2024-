n = int(input("Nhập n: "))

print(f"Các số hoàn hảo từ 1 đến {n} là:")

for num in range(1, n + 1):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num)
