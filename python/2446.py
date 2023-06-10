N = int(input())
for i in range(1, 2 * N, 2):
    print(' ' * int(i / 2) + '*' * (2 * N - i))
for i in range(3, 2 * N, 2):
    print(' ' * (N - int(i / 2) - 1) + '*' * i)