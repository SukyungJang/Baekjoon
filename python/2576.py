lis = []
count = 0
while True:
    a = int(input())
    if a % 2 == 1:
        lis.append(a)
    count += 1
    if count == 7:
        break

if len(lis) == 0:
    print(-1)
else:
    print(sum(lis), min(lis))