n = int(input())
a = int()
grade = list(map(int, input().split()))
newGrade = [grade[i]/max(grade)*100 for i in range(n)]
for i in range(n):
    a += newGrade[i]
print(a/n)