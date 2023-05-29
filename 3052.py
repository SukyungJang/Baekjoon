n = [int(input()) for _ in range(10)]
li = []
for i in range(10):
    if n[i] % 42 not in li:
        li.append(n[i]%42)
print(len(li))