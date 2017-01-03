def strLengthParity(stringList):
    lst = [0, 0]
    for i in stringList:
        lst[len(i)%2] += 1
    return lst

print(strLengthParity(['a','aa','a','a','a','aa']))
