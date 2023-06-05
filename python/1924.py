m, d = map(int, input().split())
y = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m == 1:
    e = d
else:
    e = sum(y[:m-1]) + d

a = e % 7
if a == 1:
    print('MON')
elif a == 2:
    print('TUE')
elif a == 3:
    print('WED')
elif a == 4:
    print('THU')
elif a == 5:
    print('FRI')
elif a == 6:
    print('SAT')
else:
    print('SUN')