s = list(map(str, input().split()))
set = set()
print(s)
for i in s:
    for j in i:
        set.add(j)

print(list(set))
