li = []
for i in range(3):
    a = int(input())
    li.append(a)

if (li[0] == 60) and (li[1] == 60) and (li[2] == 60):
    print('Equilateral')
elif ((li[0] == li[1]) or (li[1] == li[2]) or (li[0] == li[2])) and (li[0] + li[1] + li[2]) == 180:
    print('Isosceles')
elif (li[0] != li[1] != li[2]) and (li[0] + li[1] + li[2]) == 180:
    print('Scalene')
elif (li[0] + li[1] + li[2]) != 180:
    print('Error')