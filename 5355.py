t = int(input())
b = float()

for i in range(t):
    a = list(input().split())
    b = float(a[0])
    for j in range(1, len(a)):
        if a[j] == '@':
            b *= 3
        elif a[j] == '%':
            b += 5
        elif a[j] == '#':
            b -= 7
        else:
            b += float(a[j])
    print("{:.2f}".format(float(b)))