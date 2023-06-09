N = int(input())
for i in range(1, N * 2 + 1, 2):
    print(' ' * (N - int(i/2) - 1) + ('*' * i))