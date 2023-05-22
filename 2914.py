import math

a, i = map(int, input().split())
print(math.ceil(a * (i - 0.9999999)))