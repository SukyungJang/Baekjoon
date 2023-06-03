n = [i for i in range(1, 31)] # 1부터
a = [int(input()) for _ in range(len(n)-2)]

for i in range(len(n)):
    if n[i] not in a:
        print(n[i])