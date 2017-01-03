def vowelDict(text):
    text = text.lower()
    words = text.split()
    vowels = "aeiou"
    dic = {}
    for vowel in vowels:
        lst = []
        for word in words:
            if vowel in word:
                lst.append(word)
        dic[vowel] = set(lst)
    return dic

print(vowelDict("we need more and more practice"), sep="\n")
