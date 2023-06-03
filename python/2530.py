hour, minute, second = map(int, input().split())
plus = int(input())

if second + plus >= 60:
    minute += (second + plus) // 60
    second = (second + plus) % 60
else:
    second += plus
if minute >= 60:
    hour += minute // 60
    minute = minute % 60
if hour >= 24:
    hour = hour % 24

print(hour, minute, second)