S = input()
string = 'abcdefghijklmnopqrstuvwxyz'
li = []
for i in string:
    if i in S:
        li.append(S.index(i))
    else:
        li.append(-1)
print(*li)