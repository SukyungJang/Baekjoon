s = int(input())
sum = 0
c = 0

for i in range(1, s + 1):
    sum += i
    c += 1
    if s == 2:
        print(1)
        break
    if sum == s:
        print(c)
        break
    elif sum > s:
        print(c - 1)
        break