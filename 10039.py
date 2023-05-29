score = []
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    score.append(a)

meanScore = int()
for i in range(len(score)):
    meanScore += score[i]
print(int(meanScore/5))