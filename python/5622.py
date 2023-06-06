d = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", "0"]
s = input()
t_cnt = 0
for i in s:
    cnt = 2
    for j in d:
        if j.find(i) != -1:
            break
        cnt += 1
    t_cnt += cnt
print(t_cnt)