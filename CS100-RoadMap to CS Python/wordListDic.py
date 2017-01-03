wordOccurances =[('rabbit', 1), ('Alice', 2), ('Alice', 3)]

def makeIndex(wordPageList):
    wordIndex={}
    for i in wordPageList:
        if i[0] in wordIndex:
            wordIndex[i[0]].append(i[1])
        else:
            wordIndex[i[0]] = [i[1]]
    return wordIndex

print(makeIndex(wordOccurances))
