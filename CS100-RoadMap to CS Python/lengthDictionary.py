def lengthDictionary(text):
    dic = {}
    text = text.lower()
    text = text.split()
    for i in text:
        if len(i) not in dic:
            dic[len(i)] = [i]
        elif len(i) in dic and i not in dic[len(i)]:
            dic[len(i)].append(i)
    return dic

string = '''
The Dear John punctuation example is a very commonly
used story about a man who received a beautiful letter from his loved one
In the letter his girlfriend spelled out in no uncertain terms
how much she loved and adored John and it was clear to anyone reading
her words that she couldnt
live without him Or could she
'''
print(lengthDictionary(string))
