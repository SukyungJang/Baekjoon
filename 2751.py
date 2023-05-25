import sys
n = int(input())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()
print(*li)