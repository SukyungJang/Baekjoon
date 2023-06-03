li = []
for i in range(9):
    li.append(int(input()))

for idx, n in enumerate(li):
    if n == max(li):
        print(n)
        print(idx + 1)