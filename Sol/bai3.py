n = int(input())
l = []
for _ in range(n):
    name, score = input().split()
    l.append((name, int(score)))

s = set()
for name, score in l:
    s.add(score)

score_list = list(sorted(s))
for name, score in l:
    if score == score_list[1]:
        print(name)
    