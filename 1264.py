while True:
    sen = input()
    count = 0
    if sen == '#':
        break
    for i in range(len(sen)):
        if sen[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(count)