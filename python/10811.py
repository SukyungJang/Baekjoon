n, m = map(int, input().split())
basket = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    if i < j:
        ist = basket[i-1:j-1]; jst = basket[j-1:i-1:-1]
        basket[i-1:j-1] = jst; basket[j-1:i-1:-1] = ist

print(*basket)