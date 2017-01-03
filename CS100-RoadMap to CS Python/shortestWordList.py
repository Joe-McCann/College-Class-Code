def shortestWord(wordsList):
    short = wordsList[0]
    for i in wordsList:
        if len(short) > len(i):
            short = i

    return short

print(shortestWord(["bob", "bb", "a", "aaa"]))
