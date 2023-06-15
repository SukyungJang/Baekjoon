li = []
for i in range(5):
    a = int(input())
    li.append(a)

li_sorted = sorted(li)

print(int(sum(li)/5))
print(li_sorted[len(li_sorted) // 2])