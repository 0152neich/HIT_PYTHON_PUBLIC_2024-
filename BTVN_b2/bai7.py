N = int(input("Nhập N: "))

print(f"Các cặp số Amicable từ 1 đến {N} là:")

for a in range(1, N + 1):
    sum_a = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a += i

    b = sum_a
    
    if b > a and b <= N:
        sum_b = 0
        for i in range(1, b):
            if b % i == 0:
                sum_b += i

        if sum_b == a:
            print(f"({a}, {b})")
