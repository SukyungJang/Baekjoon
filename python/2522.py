N = int(input())
for i in range(1, N + 1):
    print(('*' * i).rjust(N))
for i in range(1, N):
    print(('*' * (N -i)).rjust(N))