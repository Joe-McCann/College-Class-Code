def wordsInVowel(wordsList):
    vowels = 'aeiou'
    count = 0
    for i in wordsList:
        string = i.lower()
        if string[0] in vowels:
            count += 1
    return count

print(wordsInVowel(['Joe', 'aaa', 'bbb', 'Eee']))
