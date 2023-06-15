chess = [1, 1, 2, 2, 2, 8]
mine = list(map(int, input().split()))
li = []
for i in range(len(chess)):
    li.append(chess[i] - mine[i])
print(*li)