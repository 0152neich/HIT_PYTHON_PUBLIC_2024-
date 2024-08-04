n, m = map(int, input("Nhập n và m: ").split())

array = list(map(int, input("Nhập các phần tử của mảng: ").split()))
A = set(map(int, input("Nhập các phần tử của tập hợp A: ").split()))
B = set(map(int, input("Nhập các phần tử của tập hợp B: ").split()))

happiness = 0

for num in array:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1  
print("Mức độ hạnh phúc cuối cùng:", happiness)
