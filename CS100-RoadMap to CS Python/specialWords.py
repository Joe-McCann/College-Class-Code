def specialWords(wordList):
    lst = []
    for i in wordList:
        if i[0] == i[-1] and i not in lst:
            lst.append(i)
    return lst

print(specialWords(['aha', 'aha', 'bb', 'cd', 'tq']))
