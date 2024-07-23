n = int(input("Nhập n: "))

print(f"Các số Armstrong bậc 3 từ 1 đến {n} là:")

for num in range(1, n + 1):
    t = num
    sum = 0
    while t > 0:
        digit = t % 10
        sum += digit ** 3
        t //= 10

    if sum == num:
        print(num)