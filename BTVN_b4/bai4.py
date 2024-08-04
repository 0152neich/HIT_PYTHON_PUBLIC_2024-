n = int(input())
s = {int(input()) for _ in range(n)}
k = int(input())
s1 = set()
m = 0
for i in list(s):
    m += i
    if m > k:
        continue
    s1.add(i)
print(s1)