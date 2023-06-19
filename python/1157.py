from collections import Counter

a = input().upper()
n = 0
s = ''

for i, j in Counter(a).items(): # (문자, 빈도)
    if j == n:
        s = '?'
    elif j > n:
        n = j
        s = i
print(s)