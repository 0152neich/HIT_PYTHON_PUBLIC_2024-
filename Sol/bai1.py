# Bài 1
t = tuple(map(int, input().split()))
result = set()
for x in t:
    if t.count(x) % 5 == 0 and t.count(x) % 10 != 0:
        result.add(x)
    
for i in list(result):
    print(i, end=' ')
