n, m = map(int, input().split())

basket = []
for num in range(n):
    basket.append(int())

for num1 in range(m):
    i, j, k = map(int, input().split())
    for num2 in range(i-1, j):
        basket[num2] = k
for num2 in basket:
    print(num2, end =' ')