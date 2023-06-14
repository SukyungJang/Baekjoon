l = [int(input()) for i in range(3)]

if sum(l) == 180:
    if l.count(60) == 3: print('Equilateral')
    elif len(set(l)) == 2: print('Isosceles')
    else: print('Scalene')
else: print('Error')