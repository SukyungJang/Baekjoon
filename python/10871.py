N, X = map(int, input().split())
A = list(map(int, input().split()))
t = []
for i in range(len(A)):
    if A[i] < X:
        t.append(A[i])
print(*t)