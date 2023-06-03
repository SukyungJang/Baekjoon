h, m = map(int, input().split())
minute = int(input())

if m + minute >= 60:
    h += (m + minute) // 60
    m = (m + minute) % 60
else:
    m += minute
if h >= 24:
    h = h - 24

print(h, m)