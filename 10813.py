n, m = map(int, input().split())
basket = [num + 1 for num in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    if i < j:
        ia = basket[i-1]; ja = basket[j-1]
        basket[i-1] = ja; basket[j-1] = ia

print(*basket)