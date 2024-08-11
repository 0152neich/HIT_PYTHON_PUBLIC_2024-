n = int(input())
a = list(map(int, input().split()))
j = 0
for i in range(n):
    if a[i] == i + 1 + j:
        j += 1
print(n + j)